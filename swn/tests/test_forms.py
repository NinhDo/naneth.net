from django.test import TestCase

from swn.forms import *

class UserFormTestCase(TestCase):
	def test_save(self):
		form_data = {
			"username": "test",
			"first_name": "test",
			"last_name": "test",
			"password1": "t1e2s3t4",
			"password2": "t1e2s3t4"
		}
		form = UserForm(form_data)
		self.assertTrue(form.is_valid())
		user = super(UserForm, form).save(commit = False)
		self.assertEqual(form.save(commit = True), user)
