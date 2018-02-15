from django.db import models

# Create your models here.

class AlienBodyType(models.Model):
	name = models.CharField(max_length=32)
	desc = models.TextField(blank=True)
	def __str__(self):
		return self.name


class AlienLenses(models.Model):
	name = models.CharField(max_length=32)
	desc = models.TextField(blank=True)
	def __str__(self):
		return self.name


class AlienStructure(models.Model):
	name = models.CharField(max_length=32)
	desc = models.TextField(blank=True)
	def __str__(self):
		return self.name


class AlienVarAvian(models.Model):
	variation = models.CharField(max_length=64)
	def __str__(self):
		return self.variation


class AlienVarExotic(models.Model):
	variation = models.CharField(max_length=64)
	def __str__(self):
		return self.variation


class AlienVarInsect(models.Model):
	variation = models.CharField(max_length=64)
	def __str__(self):
		return self.variation


class AlienVarMammal(models.Model):
	variation = models.CharField(max_length=64)
	def __str__(self):
		return self.variation


class AlienVarReptile(models.Model):
	variation = models.CharField(max_length=64)
	def __str__(self):
		return self.variation


class NPCAge(models.Model):
	age = models.CharField(max_length=32)
	def __str__(self):
		return self.age


class NPCGender(models.Model):
	gender = models.CharField(max_length=32)
	def __str__(self):
		return self.gender


class NPCHeight(models.Model):
	height = models.CharField(max_length=32)
	def __str__(self):
		return self.height


class NPCMotivation(models.Model):
	motive = models.CharField(max_length=64)
	def __str__(self):
		return self.motive


class NPCProblems(models.Model):
	problem = models.CharField(max_length=64)
	def __str__(self):
		return self.problem


class NPCQuirk(models.Model):
	quirk = models.CharField(max_length=64)
	def __str__(self):
		return self.quirk


class QuickArchitecture(models.Model):
	element = models.CharField(max_length=64)
	def __str__(self):
		return self.element


class QuickCorpBusiness(models.Model):
	business = models.CharField(max_length=32)
	def __str__(self):
		return self.business


class QuickCorpName(models.Model):
	name = models.CharField(max_length=32)
	organization = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class QuickCorpReputation(models.Model):
	reputation = models.CharField(max_length=64)
	def __str__(self):
		return self.reputation


class QuickHeresyAttitude(models.Model):
	attitude = models.CharField(max_length=128)
	adjective = models.CharField(max_length=32)
	def __str__(self):
		return self.adjective


class QuickHeresyFounder(models.Model):
	founder = models.CharField(max_length=128)
	def __str__(self):
		return self.founder


class QuickHeresyHeresy(models.Model):
	major_heresy = models.TextField()
	name = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class QuickHeresyQuirk(models.Model):
	quirk = models.CharField(max_length=64)
	def __str__(self):
		return self.quirk


class QuickPoliticalIssues(models.Model):
	issue = models.TextField()
	tag = models.CharField(max_length=32)
	def __str__(self):
		return self.tag


class QuickPoliticalLeadership(models.Model):
	leadership = models.TextField()
	def __str__(self):
		return self.leadership


class QuickPoliticalName(models.Model):
	element1 = models.CharField(max_length=32, unique=True)
	element2 = models.CharField(max_length=32, unique=True)


class QuickPoliticalOutsiders(models.Model):
	relationship = models.TextField()
	def __str__(self):
		return self.relationship


class QuickPoliticalPolicy(models.Model):
	policy = models.TextField()
	def __str__(self):
		return self.policy


class QuickReligionEvolution(models.Model):
	evolution = models.TextField()
	adjective = models.CharField(max_length=32)
	def __str__(self):
		return self.adjective


class QuickReligionLeadership(models.Model):
	leadership = models.TextField()
	def __str__(self):
		return self.leadership


class QuickReligionOrigin(models.Model):
	origin = models.CharField(max_length=32)
	name = models.CharField(max_length=32)
	adjective = models.CharField(max_length=32)
	def __str__(self):
		return self.origin


class QuickRoom(models.Model):
	room = models.TextField()
	def __str__(self):
		return self.room


class WorldAtmosphere(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	short = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class WorldBiosphere(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	short = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class WorldPopulation(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	short = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class WorldTag(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	enemies = models.TextField(blank=True)
	friends = models.TextField(blank=True)
	complications = models.TextField(blank=True)
	things = models.TextField(blank=True)
	places = models.TextField(blank=True)
	short = models.CharField(max_length=32, null=True)

	def __str__(self):
		return self.name

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in WorldTag._meta.fields]


class WorldTechLevel(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	short = models.CharField(max_length=32)
	def __str__(self):
		return self.name


class WorldTemperature(models.Model):
	name = models.CharField(max_length=64)
	desc = models.TextField()
	short = models.CharField(max_length=32)
	def __str__(self):
		return self.name


"""
System
Name
Nav Designation
"""
class System(models.Model):
	name = models.CharField(max_length=200)
	alias = models.CharField(max_length=128)
	nav_designation = models.CharField(max_length=50)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name


"""
Planet
Name
Nav Designation
Atmosphere
Temperature
Biosphere
Population
Tech Level
Tags
"""
class Planet(models.Model):
	system = models.ForeignKey('System', on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	alias = models.CharField(max_length=128)
	system_name_designation = models.CharField(max_length=64)
	atmosphere = models.ForeignKey('WorldAtmosphere', on_delete=models.CASCADE)
	temperature = models.ForeignKey('WorldTemperature', on_delete=models.CASCADE)
	biosphere = models.ForeignKey('WorldBiosphere', on_delete=models.CASCADE)
	population = models.ForeignKey('WorldPopulation', on_delete=models.CASCADE)
	tech_level = models.ForeignKey('WorldTechLevel', on_delete=models.CASCADE)
	tag1 = models.ForeignKey('WorldTag', on_delete=models.CASCADE, null=True)
	tag2 = models.ForeignKey('WorldTag', on_delete=models.CASCADE, null=True, related_name="+")
	capital_and_government = models.TextField(blank=True)
	cultural_notes = models.TextField(blank=True)
	adventures_prepared = models.TextField(blank=True)
	party_activities_on_this_world = models.TextField(blank=True)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

"""
Alien Races
Name
Body Type
Lenses
Structure
"""
class Alien(models.Model):
	name = models.CharField(max_length=200)
	body_type = models.ForeignKey('AlienBodyType', on_delete=models.CASCADE)
	lenses1 = models.ForeignKey('AlienLenses', on_delete=models.CASCADE)
	lenses2 = models.ForeignKey('AlienLenses', on_delete=models.CASCADE, related_name="+")
	structure1 = models.ForeignKey('AlienStructure', on_delete=models.CASCADE)
	structure2 = models.ForeignKey('AlienStructure', on_delete=models.CASCADE, related_name="+", null=True, blank=True)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

"""
Corporation
Name
Business
Reputation
"""
class Corporation(models.Model):
	name = models.CharField(max_length=200)
	business = models.ForeignKey('QuickCorpBusiness', on_delete=models.CASCADE)
	reputation = models.ForeignKey('QuickCorpReputation', on_delete=models.CASCADE)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

"""
Political Group
Name
Leadership
Policy
Outsiders
Key Issues
"""
class PoliticalGroup(models.Model):
	name = models.CharField(max_length=200)
	leadership = models.ForeignKey('QuickPoliticalLeadership', on_delete=models.CASCADE)
	policy = models.ForeignKey('QuickPoliticalPolicy', on_delete=models.CASCADE)
	outsiders = models.ForeignKey('QuickPoliticalOutsiders', on_delete=models.CASCADE)
	key_issue1 = models.ForeignKey('QuickPoliticalIssues', on_delete=models.CASCADE)
	key_issue2 = models.ForeignKey('QuickPoliticalIssues', on_delete=models.CASCADE, related_name="+")
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

"""
Religion
Name
Origin
Leadership
"""
class Religion(models.Model):
	name = models.CharField(max_length=200)
	origin = models.ForeignKey('QuickReligionOrigin', on_delete=models.CASCADE)
	leadership = models.ForeignKey('QuickReligionLeadership', on_delete=models.CASCADE)
	evolution = models.ForeignKey('QuickReligionEvolution', on_delete=models.CASCADE)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

class Heresy(models.Model):
	religion = models.ForeignKey('Religion', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	founder = models.ForeignKey('QuickHeresyFounder', on_delete=models.CASCADE)
	quirk = models.ForeignKey('QuickHeresyQuirk', on_delete=models.CASCADE)
	major_heresy = models.ForeignKey('QuickHeresyHeresy', on_delete=models.CASCADE)
	attitude_towards_orthodoxt = models.ForeignKey('QuickHeresyAttitude', on_delete=models.CASCADE)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

"""
NPC
Name
Gender
Age
Height
Quirk
Motive
Problem
"""
class NPC(models.Model):
	name = models.CharField(max_length=200)
	gender = models.ForeignKey('NPCGender', on_delete=models.CASCADE)
	age = models.ForeignKey('NPCAge', on_delete=models.CASCADE)
	height = models.ForeignKey('NPCHeight', on_delete=models.CASCADE)
	quirk = models.ForeignKey('NPCQuirk', on_delete=models.CASCADE)
	motivation = models.ForeignKey('NPCMotivation', on_delete=models.CASCADE)
	problem = models.ForeignKey('NPCProblems', on_delete=models.CASCADE)
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

class Asset(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField()
	asset_attribute = models.CharField(max_length=128)
	hp = models.IntegerField()
	cost = models.IntegerField()
	tl = models.IntegerField()
	asset_type = models.CharField(max_length=32)
	attack = models.CharField(max_length=16)
	counterattack = models.CharField(max_length=16)
	special = models.CharField(max_length=8)
	def __str__(self):
		return self.name


class Faction_Tag(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField()
	def __str__(self):
		return self.name


class Faction_Goal(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField()
	def __str__(self):
		return self.name


class Faction(models.Model):
	name = models.CharField(max_length=128)
	alias = models.CharField(max_length=128)
	faction_type = models.CharField(max_length=128)
	force = models.IntegerField()
	cunning = models.IntegerField()
	wealth = models.IntegerField()
	current_hp = models.IntegerField()
	max_hp = models.IntegerField()
	income = models.IntegerField()
	faccreds = models.IntegerField()
	tags = models.ManyToManyField(Faction_Tag)
	goal = models.ForeignKey("Faction_Goal", on_delete=models.SET_NULL, null=True, blank=True)
	homeworld = models.ForeignKey("Planet", on_delete=models.SET_NULL, null=True, blank=True)
	exp = models.IntegerField(default=0)
	pc_reputation = models.CharField(max_length=32, default="Neutral")
	notes = models.ForeignKey("Notes", on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name

class Faction_Asset(models.Model):
	owner = models.ForeignKey("Faction", on_delete=models.SET_NULL, null=True)
	asset = models.ForeignKey("Asset", on_delete=models.SET_NULL, null=True)
	current_hp = models.IntegerField(default=0)
	location = models.ForeignKey("Planet", on_delete=models.CASCADE)
	status = models.CharField(max_length=32, blank=True, null=True)
	def __str__(self):
		return "{} - {}".format(self.owner, self.asset)


class Notes(models.Model):
	player_notes = models.TextField(blank="True", default="")
	gm_notes = models.TextField(blank="True", default="")
