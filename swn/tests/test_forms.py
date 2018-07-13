from django.test import TestCase

from django.contrib.auth.forms import UserCreationForm

from swn.forms import *

class UserFormTestCase(TestCase):
	def test_save(self):
		form_data = {
			"username": "test",
			"first_name": "test",
			"last_name": "test",
			"password1": "test1234",
			"password2": "test1234"
		}
		form = UserForm(data = form_data)
		self.assertTrue(form.is_valid())
		user = super(UserForm, form).save(commit = False)
		self.assertEqual(form.save(commit = True), user)
