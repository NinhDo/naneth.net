import hmac
from hashlib import sha1
from decouple import config

from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from django.utils.encoding import force_bytes

from api.views import *

class helloTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()

	def test_get(self):
		request = self.factory.get(reverse("api:hello"))
		response = hello(request)
		self.assertEqual(response.status_code, 405)

	def test_no_ip(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = None
		request.META["HTTP_X_REAL_IP"] = None

		response = hello(request)
		self.assertEqual(response.status_code, 501)
		self.assertEqual(response.content, b'No IP address.')

	def test_wrong_remote_addr(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "127.0.0.1"
		request.META["HTTP_X_REAL_IP"] = None

		response = hello(request)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.content, b'Permission denied.')

	def test_wrong_http_x_real_ip(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = None
		request.META["HTTP_X_REAL_IP"] = "127.0.0.1"

		response = hello(request)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.content, b'Permission denied.')

	def test_no_header_signature(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "192.30.252.0"
		request.META["HTTP_X_REAL_IP"] = "192.30.252.0"
		request.META["HTTP_X_HUB_SIGNATURE"] = None

		response = hello(request)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.content, b'Permission denied.')

	def test_not_sha1(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "192.30.252.0"
		request.META["HTTP_X_REAL_IP"] = "192.30.252.0"
		request.META["HTTP_X_HUB_SIGNATURE"] = "test=test"

		response = hello(request)
		self.assertEqual(response.status_code, 501)
		self.assertEqual(response.content, b'Operation not supported.')

	def test_no_mac(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "192.30.252.0"
		request.META["HTTP_X_REAL_IP"] = "192.30.252.0"
		request.META["HTTP_X_HUB_SIGNATURE"] = "sha1=test"

		response = hello(request)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.content, b'Permission denied.')

	def test_ping(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "192.30.252.0"
		request.META["HTTP_X_REAL_IP"] = "192.30.252.0"
		request.META["HTTP_X_GITHUB_EVENT"] = "ping"
		request.content_type = "application/json"
		mac = hmac.new(force_bytes(config('GITHUB_WEBHOOK_KEY')), msg=force_bytes(request.body), digestmod=sha1)
		request.META["HTTP_X_HUB_SIGNATURE"] = "sha1=" + mac.hexdigest()
		response = hello(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'pong')

	def test_push(self):
		request = self.factory.post(reverse("api:hello"))
		request.META["REMOTE_ADDR"] = "192.30.252.0"
		request.META["HTTP_X_REAL_IP"] = "192.30.252.0"
		request.META["HTTP_X_GITHUB_EVENT"] = "push"
		request.content_type = "application/json"
		mac = hmac.new(force_bytes(config('GITHUB_WEBHOOK_KEY')), msg=force_bytes(request.body), digestmod=sha1)
		request.META["HTTP_X_HUB_SIGNATURE"] = "sha1=" + mac.hexdigest()
		response = hello(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'success')
