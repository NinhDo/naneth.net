from django.test import TestCase
from django.contrib.auth.models import User, Group
from swn.templatetags.template_tags import *

class has_groupTestCase(TestCase):
	def test_rendered(self):
		g = Group.objects.create(name="GM")
		user = User.objects.create_user("test", "test@test.com", "testpassword")
		g.user_set.add(user)
		self.assertTrue(has_group(user, "GM"))
