from django.test import TestCase

from swn.models import *

class AlienBodyTypeTestCase(TestCase):
	def setUp(self):
		AlienBodyType.objects.create(name = "A name", desc = "A description")

	def test_str(self):
		m = AlienBodyType.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class AlienLensesTestCase(TestCase):
	def setUp(self):
		AlienLenses.objects.create(name = "A name", desc = "A description")

	def test_str(self):
		m = AlienLenses.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class AlienStructureTestCase(TestCase):
	def setUp(self):
		AlienStructure.objects.create(name = "A name", desc = "A description")

	def test_str(self):
		m = AlienStructure.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class AlienVarAvianTestCase(TestCase):
	def setUp(self):
		AlienVarAvian.objects.create(variation = "A variation")

	def test_str(self):
		m = AlienVarAvian.objects.get(variation = "A variation")
		self.assertEqual(str(m), m.variation)

class AlienVarExoticTestCase(TestCase):
	def setUp(self):
		AlienVarExotic.objects.create(variation = "A variation")

	def test_str(self):
		m = AlienVarExotic.objects.get(variation = "A variation")
		self.assertEqual(str(m), m.variation)

class AlienVarInsectTestCase(TestCase):
	def setUp(self):
		AlienVarInsect.objects.create(variation = "A variation")

	def test_str(self):
		m = AlienVarInsect.objects.get(variation = "A variation")
		self.assertEqual(str(m), m.variation)

class AlienVarMammalTestCase(TestCase):
	def setUp(self):
		AlienVarMammal.objects.create(variation = "A variation")

	def test_str(self):
		m = AlienVarMammal.objects.get(variation = "A variation")
		self.assertEqual(str(m), m.variation)

class AlienVarReptileTestCase(TestCase):
	def setUp(self):
		AlienVarReptile.objects.create(variation = "A variation")

	def test_str(self):
		m = AlienVarReptile.objects.get(variation = "A variation")
		self.assertEqual(str(m), m.variation)

class NPCAgeTestCase(TestCase):
	def setUp(self):
		NPCAge.objects.create(age = "An age")

	def test_str(self):
		m = NPCAge.objects.get(age = "An age")
		self.assertEqual(str(m), m.age)

class NPCGenderTestCase(TestCase):
	def setUp(self):
		NPCGender.objects.create(gender = "A gender")

	def test_str(self):
		m = NPCGender.objects.get(gender = "A gender")
		self.assertEqual(str(m), m.gender)

class NPCHeightTestCase(TestCase):
	def setUp(self):
		NPCHeight.objects.create(height = "A height")

	def test_str(self):
		m = NPCHeight.objects.get(height = "A height")
		self.assertEqual(str(m), m.height)

class NPCMotivationTestCase(TestCase):
	def setUp(self):
		NPCMotivation.objects.create(motive = "A motive")

	def test_str(self):
		m = NPCMotivation.objects.get(motive="A motive")
		self.assertEqual(str(m), m.motive)

class NPCProblemsTestCase(TestCase):
	def setUp(self):
		NPCProblems.objects.create(problem = "A problem")

	def test_str(self):
		m = NPCProblems.objects.get(problem="A problem")
		self.assertEqual(str(m), m.problem)

class NPCQuirkTestCase(TestCase):
	def setUp(self):
		NPCQuirk.objects.create(quirk = "A quirk")

	def test_str(self):
		m = NPCQuirk.objects.get(quirk="A quirk")
		self.assertEqual(str(m), m.quirk)

class QuickArchitectureTestCase(TestCase):
	def setUp(self):
		QuickArchitecture.objects.create(element = "A element")

	def test_str(self):
		m = QuickArchitecture.objects.get(element="A element")
		self.assertEqual(str(m), m.element)

class QuickCorpBusinessTestCase(TestCase):
	def setUp(self):
		QuickCorpBusiness.objects.create(business = "A business")

	def test_str(self):
		m = QuickCorpBusiness.objects.get(business="A business")
		self.assertEqual(str(m), m.business)

class QuickCorpNameTestCase(TestCase):
	def setUp(self):
		QuickCorpName.objects.create(name = "A name", organization = "An organization")

	def test_str(self):
		m = QuickCorpName.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class QuickCorpReputationTestCase(TestCase):
	def setUp(self):
		QuickCorpReputation.objects.create(reputation = "A reputation")

	def test_str(self):
		m = QuickCorpReputation.objects.get(reputation="A reputation")
		self.assertEqual(str(m), m.reputation)

class QuickHeresyAttitudeTestCase(TestCase):
	def setUp(self):
		QuickHeresyAttitude.objects.create(attitude = "An attitude", adjective = "An adjective")

	def test_str(self):
		m = QuickHeresyAttitude.objects.get(adjective = "An adjective")
		self.assertEqual(str(m), m.adjective)

class QuickHeresyFounderTestCase(TestCase):
	def setUp(self):
		QuickHeresyFounder.objects.create(founder = "A founder")

	def test_str(self):
		m = QuickHeresyFounder.objects.get(founder="A founder")
		self.assertEqual(str(m), m.founder)

class QuickHeresyHeresyTestCase(TestCase):
	def setUp(self):
		QuickHeresyHeresy.objects.create(major_heresy = "A major heresy", name = "A name")

	def test_str(self):
		m = QuickHeresyHeresy.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class QuickHeresyQuirkTestCase(TestCase):
	def setUp(self):
		QuickHeresyQuirk.objects.create(quirk = "A quirk")

	def test_str(self):
		m = QuickHeresyQuirk.objects.get(quirk="A quirk")
		self.assertEqual(str(m), m.quirk)

class QuickPoliticalIssuesTestCase(TestCase):
	def setUp(self):
		QuickPoliticalIssues.objects.create(issue = "An issue", tag = "A tag")

	def test_str(self):
		m = QuickPoliticalIssues.objects.get(tag="A tag")
		self.assertEqual(str(m), m.tag)

class QuickPoliticalLeadershipTestCase(TestCase):
	def setUp(self):
		QuickPoliticalLeadership.objects.create(leadership = "A leadership")

	def test_str(self):
		m = QuickPoliticalLeadership.objects.get(leadership="A leadership")
		self.assertEqual(str(m), m.leadership)

class QuickPoliticalOutsidersTestCase(TestCase):
	def setUp(self):
		QuickPoliticalOutsiders.objects.create(relationship = "A relationship")

	def test_str(self):
		m = QuickPoliticalOutsiders.objects.get(relationship="A relationship")
		self.assertEqual(str(m), m.relationship)

class QuickPoliticalPolicyTestCase(TestCase):
	def setUp(self):
		QuickPoliticalPolicy.objects.create(policy = "A policy")

	def test_str(self):
		m = QuickPoliticalPolicy.objects.get(policy="A policy")
		self.assertEqual(str(m), m.policy)

class QuickReligionEvolutionTestCase(TestCase):
	def setUp(self):
		QuickReligionEvolution.objects.create(evolution = "An evolution", adjective = "An adjective")

	def test_str(self):
		m = QuickReligionEvolution.objects.get(adjective="An adjective")
		self.assertEqual(str(m), m.adjective)

class QuickReligionLeadershipTestCase(TestCase):
	def setUp(self):
		QuickReligionLeadership.objects.create(leadership = "A leadership")

	def test_str(self):
		m = QuickReligionLeadership.objects.get(leadership="A leadership")
		self.assertEqual(str(m), m.leadership)

class QuickReligionOriginTestCase(TestCase):
	def setUp(self):
		QuickReligionOrigin.objects.create(origin = "A origin", name = "A name", adjective = "An adjective")

	def test_str(self):
		m = QuickReligionOrigin.objects.get(origin="A origin")
		self.assertEqual(str(m), m.origin)

class QuickRoomTestCase(TestCase):
	def setUp(self):
		QuickRoom.objects.create(room = "A room")

	def test_str(self):
		m = QuickRoom.objects.get(room="A room")
		self.assertEqual(str(m), m.room)

class WorldAtmosphereTestCase(TestCase):
	def setUp(self):
		WorldAtmosphere.objects.create(name = "A name", desc = "A description", short = "A short")

	def test_str(self):
		m = WorldAtmosphere.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class WorldBiosphereTestCase(TestCase):
	def setUp(self):
		WorldBiosphere.objects.create(name = "A name", desc = "A description", short = "A short")

	def test_str(self):
		m = WorldBiosphere.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class WorldPopulationTestCase(TestCase):
	def setUp(self):
		WorldPopulation.objects.create(name = "A name", desc = "A description", short = "A short")

	def test_str(self):
		m = WorldPopulation.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class WorldTagTestCase(TestCase):
	def setUp(self):
		WorldTag.objects.create(name = "A name", desc = "A description")

	def test_str(self):
		m = WorldTag.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

	def test_get_fields(self):
		m = WorldTag.objects.get(name="A name")
		self.assertEqual(m.get_fields(), [('id', '3'), ('name', 'A name'), ('desc', 'A description'), ('enemies', ''), ('friends', ''), ('complications', ''), ('things', ''), ('places', ''), ('short', 'None')])

class WorldTechLevelTestCase(TestCase):
	def setUp(self):
		WorldTechLevel.objects.create(name = "A name", desc = "A description", short = "A short")

	def test_str(self):
		m = WorldTechLevel.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class WorldTemperatureTestCase(TestCase):
	def setUp(self):
		WorldTemperature.objects.create(name = "A name", desc = "A description", short = "A short")

	def test_str(self):
		m = WorldTemperature.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class SystemTestCase(TestCase):
	def setUp(self):
		System.objects.create(name = "A name", alias = "An alias", nav_designation = "A nav_designation")

	def test_str(self):
		m = System.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class PlanetTestCase(TestCase):
	def setUp(self):
		system = System.objects.create(name = "A name", alias = "An alias", nav_designation = "A nav_designation")
		atmosphere = WorldAtmosphere.objects.create(name = "A name", desc = "A description", short = "A short")
		temperature = WorldTemperature.objects.create(name = "A name", desc = "A description", short = "A short")
		biosphere = WorldBiosphere.objects.create(name = "A name", desc = "A description", short = "A short")
		population = WorldPopulation.objects.create(name = "A name", desc = "A description", short = "A short")
		tech_level = WorldTechLevel.objects.create(name = "A name", desc = "A description", short = "A short")
		tag = WorldTag.objects.create(name = "A name", desc = "A description", )
		Planet.objects.create(system = system, name = "A name", alias = "An alias", system_name_designation = "A system name designation", atmosphere = atmosphere, temperature = temperature, biosphere = biosphere, population = population, tech_level = tech_level, tag1 = tag, tag2 = tag, capital_and_government = "", cultural_notes = "", adventures_prepared = "", party_activities_on_this_world = "")

	def test_str(self):
		m = Planet.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class AlienTestCase(TestCase):
	def setUp(self):
		bt = AlienBodyType.objects.create(name = "A name", desc = "A description")
		l = AlienLenses.objects.create(name = "A name", desc = "A description")
		s = AlienStructure.objects.create(name = "A name", desc = "A description")
		Alien.objects.create(name = "A name", body_type = bt, lenses1 = l, lenses2 = l, structure1 = s, structure2 = s)

	def test_str(self):
		m = Alien.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class CorporationTestCase(TestCase):
	def setUp(self):
		business = QuickCorpBusiness.objects.create(business = "A business")
		reputation = QuickCorpReputation.objects.create(reputation = "A reputation")
		Corporation.objects.create(name = "A name", business = business, reputation = reputation)

	def test_str(self):
		m = Corporation.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class PoliticalGroupTestCase(TestCase):
	def setUp(self):
		leadership = QuickPoliticalLeadership.objects.create(leadership = "A leadership")
		policy = QuickPoliticalPolicy.objects.create(policy = "A policy")
		outsiders = QuickPoliticalOutsiders.objects.create(relationship = "A relationship")
		issue = QuickPoliticalIssues.objects.create(issue = "An issue", tag = "A tag")
		PoliticalGroup.objects.create(name = "A name", leadership = leadership, policy = policy, outsiders=  outsiders, key_issue1 = issue, key_issue2 = issue)

	def test_str(self):
		m = PoliticalGroup.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class ReligionTestCase(TestCase):
	def setUp(self):
		origin = QuickReligionOrigin.objects.create(origin = "An origin", name  = "A name", adjective = "An adjective")
		leadership = QuickReligionLeadership.objects.create(leadership = "A leadership")
		evolution = QuickReligionEvolution.objects.create(evolution = "An evolution", adjective = "an adjective")
		Religion.objects.create(name = "A name", origin = origin, leadership = leadership, evolution = evolution)

	def test_str(self):
		m = Religion.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class HeresyTestCase(TestCase):
	def setUp(self):
		rel_origin = QuickReligionOrigin.objects.create(origin = "An origin", name  = "A name", adjective = "An adjective")
		rel_leadership = QuickReligionLeadership.objects.create(leadership = "A leadership")
		rel_evolution = QuickReligionEvolution.objects.create(evolution = "An evolution", adjective = "an adjective")
		religion = Religion.objects.create(name = "A name", origin = rel_origin, leadership = rel_leadership, evolution = rel_evolution)
		founder = QuickHeresyFounder.objects.create(founder = "A founder")
		quirk = QuickHeresyQuirk.objects.create(quirk = "A quirk")
		major_heresy = QuickHeresyHeresy.objects.create(major_heresy = "A major heresy", name = "A name")
		attitude_towards_orthodoxt = QuickHeresyAttitude.objects.create(attitude = "An attitude", adjective = "An adjective")
		Heresy.objects.create(religion = religion, name = "A name", founder = founder, quirk = quirk, major_heresy = major_heresy, attitude_towards_orthodoxt = attitude_towards_orthodoxt)

	def test_str(self):
		m = Heresy.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class NPCTestCase(TestCase):
	def setUp(self):
		gender = NPCGender.objects.create(gender = "A gender")
		age = NPCAge.objects.create(age = "An age")
		height = NPCHeight.objects.create(height = "A height")
		quirk = NPCQuirk.objects.create(quirk = "A quirk")
		motivation = NPCMotivation.objects.create(motive = "A motivation")
		problem = NPCProblems.objects.create(problem = "A problem")
		NPC.objects.create(name = "A name", gender = gender, age = age, height = height, quirk = quirk, motivation = motivation, problem = problem)

	def test_str(self):
		m = NPC.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class AssetTestCase(TestCase):
	def setUp(self):
		Asset.objects.create(name = "A name", description = "A description", asset_attribute = "An asset attribute", hp = 1, cost = 1, tl = 1, asset_type = "An asset type", attack = "An A", counterattack = "A CA", special = "A S")

	def test_str(self):
		m = Asset.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class Faction_TagTestCase(TestCase):
	def setUp(self):
		Faction_Tag.objects.create(name = "A name", description = "A description")

	def test_str(self):
		m = Faction_Tag.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class Faction_GoalTestCase(TestCase):
	def setUp(self):
		Faction_Goal.objects.create(name = "A name", description = "A description")

	def test_str(self):
		m = Faction_Goal.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class FactionTestCase(TestCase):
	def setUp(self):
		Faction.objects.create(name = "A name", alias = "An alias", faction_type = "A faction type", force = 1, cunning = 1, wealth = 1, current_hp = 1, max_hp = 1, income = 1, faccreds = 1)

	def test_str(self):
		m = Faction.objects.get(name="A name")
		self.assertEqual(str(m), m.name)

class Faction_AssetTestCase(TestCase):
	def setUp(self):
		system = System.objects.create(name = "A name", alias = "An alias", nav_designation = "A nav_designation")
		atmosphere = WorldAtmosphere.objects.create(name = "A name", desc = "A description", short = "A short")
		temperature = WorldTemperature.objects.create(name = "A name", desc = "A description", short = "A short")
		biosphere = WorldBiosphere.objects.create(name = "A name", desc = "A description", short = "A short")
		population = WorldPopulation.objects.create(name = "A name", desc = "A description", short = "A short")
		tech_level = WorldTechLevel.objects.create(name = "A name", desc = "A description", short = "A short")
		tag = WorldTag.objects.create(name = "A name", desc = "A description", )
		planet = Planet.objects.create(system = system, name = "A name", alias = "An alias", system_name_designation = "A system name designation", atmosphere = atmosphere, temperature = temperature, biosphere = biosphere, population = population, tech_level = tech_level, tag1 = tag, tag2 = tag, capital_and_government = "", cultural_notes = "", adventures_prepared = "", party_activities_on_this_world = "")
		Faction_Asset.objects.create(location = planet)

	def test_str(self):
		m = Faction_Asset.objects.get(current_hp = 0)
		self.assertEqual(str(m), "{} - {}".format(m.owner, m.asset))
