from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth

from django.contrib.auth.models import User, Group

from swn.forms import UserForm
from swn.views import *

client = Client()

def create_system():
	system = System.objects.create(name = "A name", alias = "alias", nav_designation = "0000")
	return system

def create_planet():
	system = create_system()
	atmosphere = WorldAtmosphere.objects.create(name = "A name", desc = "A description", short = "A short")
	temperature = WorldTemperature.objects.create(name = "A name", desc = "A description", short = "A short")
	biosphere = WorldBiosphere.objects.create(name = "A name", desc = "A description", short = "A short")
	population = WorldPopulation.objects.create(name = "A name", desc = "A description", short = "A short")
	tech_level = WorldTechLevel.objects.create(name = "A name", desc = "A description", short = "A short")
	tag = WorldTag.objects.create(name = "A name", desc = "A description", )
	planet = Planet.objects.create(system = system, name = "A name", alias = "alias", system_name_designation = "A system name designation", atmosphere = atmosphere, temperature = temperature, biosphere = biosphere, population = population, tech_level = tech_level, tag1 = tag, tag2 = tag, capital_and_government = "", cultural_notes = "", adventures_prepared = "", party_activities_on_this_world = "")
	return planet

class user_is_gmTestCase(TestCase):
	def test_user_is_gm(self):
		user = User.objects.create_user("test", "test@test.com", "testpassword")
		group = Group.objects.create(name = "GM")
		self.assertFalse(user_is_gm(user))
		group.user_set.add(user)
		self.assertTrue(user_is_gm(user))

class indexTestCase(TestCase):
	def test_no_planet_list(self):
		response = self.client.get(reverse("swn:index"))
		self.assertEqual(response.status_code, 404)

	def test_has_planet_list(self):
		create_planet()
		response = self.client.get(reverse("swn:index"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["planet_list"], ["<Planet: A name>"])

class systemTestCase(TestCase):
	def test_no_system(self):
		response = self.client.get(reverse("swn:system", args=["alias"]))
		self.assertEqual(response.status_code, 404)

	def test_no_planet_list(self):
		create_system()
		self.test_no_system()

	def test_has_context(self):
		planet = create_planet()
		response = self.client.get(reverse("swn:system", args=["alias"]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["system"], planet.system)
		self.assertQuerysetEqual(response.context["planet_list"], ["<Planet: A name>"])

class planetTestCase(TestCase):
	def test_no_system(self):
		response = self.client.get(reverse("swn:planet", args=["alias", "alias"]))
		self.assertEqual(response.status_code, 404)

	def test_has_no_planet(self):
		create_system()
		self.test_no_system()

	def test_has_context(self):
		planet = create_planet()
		response = self.client.get(reverse("swn:planet", args=["alias", "alias"]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["system"], planet.system)
		self.assertEqual(response.context["planet"], planet)

class system_listTestCase(TestCase):
	def test_no_system(self):
		response = self.client.get(reverse("swn:system_list"))
		self.assertEqual(response.status_code, 404)

	def test_has_context(self):
		system = create_system()
		response = self.client.get(reverse("swn:system_list"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["system_list"], ["<System: A name>"])

class factionTestCase(TestCase):
	def test_no_faction_list(self):
		response = self.client.get(reverse("swn:faction"))
		self.assertEqual(response.status_code, 404)

	def test_faction_list(self):
		Faction.objects.create(name = "A name", alias = "alias", faction_type = "A faction type", force = 1, cunning = 1, wealth = 1, current_hp = 1, max_hp = 1, income = 1, faccreds = 1)
		response = self.client.get(reverse("swn:faction"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["faction_list"], ["<Faction: A name>"])

class faction_overviewTestCase(TestCase):
	def test_no_faction(self):
		response = self.client.get(reverse("swn:faction_overview", args=["alias"]))
		self.assertEqual(response.status_code, 404)

	def test_has_context(self):
		faction = Faction.objects.create(name = "A name", alias = "fff", faction_type = "A faction type", force = 1, cunning = 1, wealth = 1, current_hp = 1, max_hp = 1, income = 1, faccreds = 1)
		response = self.client.get(reverse("swn:faction_overview", args=["fff"]))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["faction"], faction)

class planet_directoryTestCase(TestCase):
	def test_no_planet_list(self):
		response = self.client.get(reverse("swn:planet_directory"))
		self.assertEqual(response.status_code, 404)

	def test_has_planet_list(self):
		create_planet()
		response = self.client.get(reverse("swn:planet_directory"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["planet_list"], ["<Planet: A name>"])

class alien_racesTestCase(TestCase):
	def test_no_alien_races_list(self):
		response = self.client.get(reverse("swn:alien_races"))
		self.assertEqual(response.status_code, 404)

	def test_has_alien_races_list(self):
		bt = AlienBodyType.objects.create(name = "A name", desc = "A description")
		l = AlienLenses.objects.create(name = "A name", desc = "A description")
		s = AlienStructure.objects.create(name = "A name", desc = "A description")
		Alien.objects.create(name = "A name", body_type = bt, lenses1 = l, lenses2 = l, structure1 = s, structure2 = s)
		response = self.client.get(reverse("swn:alien_races"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["alien_races_list"], ["<Alien: A name>"])

class political_groupsTestCase(TestCase):
	def test_no_political_groups_list(self):
		response = self.client.get(reverse("swn:political_groups"))
		self.assertEqual(response.status_code, 404)

	def test_has_political_groups_list(self):
		leadership = QuickPoliticalLeadership.objects.create(leadership = "A leadership")
		policy = QuickPoliticalPolicy.objects.create(policy = "A policy")
		outsiders = QuickPoliticalOutsiders.objects.create(relationship = "A relationship")
		issue = QuickPoliticalIssues.objects.create(issue = "An issue", tag = "A tag")
		PoliticalGroup.objects.create(name = "A name", leadership = leadership, policy = policy, outsiders=  outsiders, key_issue1 = issue, key_issue2 = issue)
		response = self.client.get(reverse("swn:political_groups"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["political_groups_list"], ["<PoliticalGroup: A name>"])

class corporationsTestCase(TestCase):
	def test_no_corporations_list(self):
		response = self.client.get(reverse("swn:corporations"))
		self.assertEqual(response.status_code, 404)

	def test_has_corporations_list(self):
		business = QuickCorpBusiness.objects.create(business = "A business")
		reputation = QuickCorpReputation.objects.create(reputation = "A reputation")
		Corporation.objects.create(name = "A name", business = business, reputation = reputation)
		response = self.client.get(reverse("swn:corporations"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["corporations_list"], ["<Corporation: A name>"])

class religionsTestCase(TestCase):
	def test_no_religions_list(self):
		response = self.client.get(reverse("swn:religions"))
		self.assertEqual(response.status_code, 404)

	def test_has_religions_list(self):
		origin = QuickReligionOrigin.objects.create(origin = "An origin", name  = "A name", adjective = "An adjective")
		leadership = QuickReligionLeadership.objects.create(leadership = "A leadership")
		evolution = QuickReligionEvolution.objects.create(evolution = "An evolution", adjective = "an adjective")
		Religion.objects.create(name = "A name", origin = origin, leadership = leadership, evolution = evolution)
		response = self.client.get(reverse("swn:religions"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["religions_list"], ["<Religion: A name>"])

class npcsTestCase(TestCase):
	def test_no_npcs_list(self):
		response = self.client.get(reverse("swn:npcs"))
		self.assertEqual(response.status_code, 404)

	def test_has_npcs_list(self):
		gender = NPCGender.objects.create(gender = "A gender")
		age = NPCAge.objects.create(age = "An age")
		height = NPCHeight.objects.create(height = "A height")
		quirk = NPCQuirk.objects.create(quirk = "A quirk")
		motivation = NPCMotivation.objects.create(motive = "A motivation")
		problem = NPCProblems.objects.create(problem = "A problem")
		NPC.objects.create(name = "A name", gender = gender, age = age, height = height, quirk = quirk, motivation = motivation, problem = problem)
		response = self.client.get(reverse("swn:npcs"))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context["npcs_list"], ["<NPC: A name>"])

class signupTestCase(TestCase):
	def test_get(self):
		form_data = {
			"username": "test",
			"first_name": "test",
			"last_name": "test",
			"password1": "test1234",
			"password2": "test1234"
		}
		response = self.client.get(path=reverse("signup"), data=form_data)
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context["form"].is_valid()) # Should be a blank form

	def test_post_invalid_form(self):
		form_data = {
			"username": "test",
			"first_name": "test",
			"last_name": "test",
			"password1": "test1234",
			"password2": "test1231"
		}
		response = self.client.post(path=reverse("signup"), data=form_data)
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context["form"].is_valid()) # Should be a blank form

	def test_post_valid_form(self):
		form_data = {
			"username": "test",
			"first_name": "test",
			"last_name": "test",
			"password1": "test1234",
			"password2": "test1234"
		}

		response = self.client.post(path=reverse("signup"), data=form_data)
		self.assertEqual(response.status_code, 302) # Redirected to /space
		user = auth.get_user(self.client)
		self.assertTrue(user.is_authenticated)

class save_planet_notesTestCase(TestCase):
	def make_gm(self):
		group = Group.objects.get(name = "GM")
		group.user_set.add(self.client.user)

	def setUp(self):
		self.client.user = User.objects.create_user("test", "test@test.com", "testpassword")
		Group.objects.create(name = "GM")

	def test_not_logged_in(self):
		response = self.client.get(reverse("swn:save_planet_notes"))
		self.assertEqual(response.status_code, 302) # Should redirect

	def test_not_gm(self):
		self.client._login(self.client.user)
		response = self.client.get(reverse("swn:save_planet_notes"))
		self.assertEqual(response.status_code, 302) # Should redirect

	def test_get_incorrect_parameter(self):
		self.client._login(self.client.user)
		self.make_gm()
		response = self.client.get(reverse("swn:save_planet_notes"))
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {"error_message": "Invalid form"})

	def test_get_no_planet(self):
		self.client._login(self.client.user)
		self.make_gm()
		response = self.client.get(reverse("swn:save_planet_notes") + "?planet=99")
		self.assertEqual(response.status_code, 404)

	def test_get_has_planet(self):
		self.client._login(self.client.user)
		self.make_gm()
		planet = create_planet()
		response = self.client.get(reverse("swn:save_planet_notes") + "?planet={}".format(planet.id))
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {})

	def test_post_invalid_form(self):
		self.client._login(self.client.user)
		self.make_gm()
		planet = create_planet()
		response = self.client.post(reverse("swn:save_planet_notes") + "?planet={}".format(planet.id))
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {"error_message": "Invalid form"})

	def test_post_valid_form(self):
		self.client._login(self.client.user)
		self.make_gm()
		planet = create_planet()
		form_data = {
			"capital_and_government": "",
			"cultural_notes": "",
			"adventures_prepared": "",
			"party_activities_on_this_world": "",
		}
		response = self.client.post(reverse("swn:save_planet_notes") + "?planet={}".format(planet.id), data = form_data)
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {})

class save_notesTestCase(TestCase):
	def setUp(self):
		self.client.user = User.objects.create_user("test", "test@test.com", "testpassword")

	def test_not_logged_in(self):
		response = self.client.get(reverse("swn:save_notes"))
		self.assertEqual(response.status_code, 302) # Should redirect

	def test_get_incorrect_parameter(self):
		self.client._login(self.client.user)
		response = self.client.get(reverse("swn:save_notes"))
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {"error_message": "Invalid form"})

	def test_get_no_note(self):
		self.client._login(self.client.user)
		response = self.client.get(reverse("swn:save_notes") + "?id=99")
		self.assertEqual(response.status_code, 404)

	def test_get_has_note(self):
		self.client._login(self.client.user)
		Notes.objects.create(id = 1)
		response = self.client.get(reverse("swn:save_notes") + "?id=1")
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {})

	def test_post_invalid_form(self):
		self.client._login(self.client.user)
		Notes.objects.create(id = 1)
		response = self.client.post(reverse("swn:save_notes") + "?id=1")
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {"error_message": "Invalid form"})

	def test_post_valid_form(self):
		self.client._login(self.client.user)
		Notes.objects.create(id = 1)
		form_data = {
			"player_notes": "",
			"gm_notes": "",
		}
		response = self.client.post(reverse("swn:save_notes") + "?id=1", data = form_data)
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(str(response.content, encoding="utf8"), {})
