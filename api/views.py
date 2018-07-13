import hmac, requests, subprocess, os, time, json

from hashlib import sha1
from ipaddress import ip_address, ip_network
from decouple import config

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import force_bytes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
script_path = "/var/scripts/redeploy.sh"
whitelist_path = os.path.join(BASE_DIR, "whitelist.json")

# Create your views here.
@require_POST
@csrf_exempt
def hello(request):
	# Verify if request came from GitHub
	forwarded_for = u'{}'.format(request.META.get('REMOTE_ADDR'))
	forwarded_for2 = u'{}'.format(request.META.get('HTTP_X_REAL_IP'))
	client_ip_address = ""

	try:
		client_ip_address = ip_address(forwarded_for)
	except:
		try:
			client_ip_address = ip_address(forwarded_for2)
		except:
			return HttpResponseServerError("No IP address.", status=501)

	if os.path.exists(whitelist_path): #pragma: no cover
		# If it's been 1 hour since the file was modified, update it
		if time.time() - os.path.getmtime(whitelist_path) > 3600:
			with open(whitelist_path, "w") as f:
				whitelist = requests.get('https://api.github.com/meta').json()
				json.dump(whitelist, f)
		else: # Otherwise, use the old info
			with open(whitelist_path, "r") as f:
				whitelist = json.load(f)
	else: #pragma: no cover
		# Create file if it doesn't exist
		with open(whitelist_path, "w") as f:
			whitelist = requests.get('https://api.github.com/meta').json()
			json.dump(whitelist, f)

	for valid_ip in whitelist["hooks"]:
		if client_ip_address in ip_network(valid_ip):
			break
		else:
			return HttpResponseForbidden('Permission denied.')

	header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
	if header_signature is None:
		return HttpResponseForbidden('Permission denied.')

	sha_name, signature = header_signature.split('=')
	if sha_name != 'sha1':
		return HttpResponseServerError('Operation not supported.', status=501)

	mac = hmac.new(force_bytes(config('GITHUB_WEBHOOK_KEY')), msg=force_bytes(request.body), digestmod=sha1)
	if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
		return HttpResponseForbidden('Permission denied.')

	event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')
	if event == 'ping':
		return HttpResponse('pong')
	elif event == 'push':
		subprocess.call([script_path]) #pragma: no cover
		return HttpResponse('success')
