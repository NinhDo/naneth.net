from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

import re, math

DICE_REGEX = "((\+|\-)|(\d+|((\d*d\d+)(((d|k)(l|h)?)\d+)?)))+"

EXPERIENCE_ARRAY = [
	0,
	300,
	900,
	2700,
	6500,
	14000,
	23000,
	34000,
	48000,
	64000,
	85000,
	100000,
	120000,
	140000,
	165000,
	195000,
	225000,
	265000,
	305000,
	355000,
]

CHALLENGE_RATING_CHOICES = (
	("0", "0"),
	("1/8", "1/8"),
	("1/4", "1/4"),
	("1/2", "1/2"),
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5"),
	("6", "6"),
	("7", "7"),
	("8", "8"),
	("9", "9"),
	("10", "10"),
	("11", "11"),
	("12", "12"),
	("13", "13"),
	("14", "14"),
	("15", "15"),
	("16", "16"),
	("17", "17"),
	("18", "18"),
	("19", "19"),
	("20", "20"),
	("21", "21"),
	("22", "22"),
	("23", "23"),
	("24", "24"),
	("25", "25"),
	("26", "26"),
	("27", "27"),
	("28", "28"),
	("29", "29"),
	("30", "30"),
)

CHALLENGE_RATING_EXPERIENCE = {
	"0": 10,
	"1/8": 25,
	"1/4": 50,
	"1/2": 100,
	"1": 200,
	"2": 450,
	"3": 700,
	"4": 1100,
	"5": 1800,
	"6": 2300,
	"7": 2900,
	"8": 3900,
	"9": 5000,
	"10": 5900,
	"11": 7200,
	"12": 8400,
	"13": 10000,
	"14": 11500,
	"15": 13000,
	"16": 15000,
	"17": 18000,
	"18": 20000,
	"19": 22000,
	"20": 25000,
	"21": 33000,
	"22": 41000,
	"23": 50000,
	"24": 62000,
	"25": 75000,
	"26": 90000,
	"27": 105000,
	"28": 120000,
	"29": 135000,
	"30": 155000,
}

CANTRIP       = 0
SPELL_LEVEL_1 = 1
SPELL_LEVEL_2 = 1
SPELL_LEVEL_3 = 3
SPELL_LEVEL_4 = 4
SPELL_LEVEL_5 = 5
SPELL_LEVEL_6 = 6
SPELL_LEVEL_7 = 7
SPELL_LEVEL_8 = 8
SPELL_LEVEL_9 = 9

SPELL_LEVEL_CHOICES = (
	(CANTRIP, "Cantrip"),
	(SPELL_LEVEL_1, "1"),
	(SPELL_LEVEL_2, "2"),
	(SPELL_LEVEL_3, "3"),
	(SPELL_LEVEL_4, "4"),
	(SPELL_LEVEL_5, "5"),
	(SPELL_LEVEL_6, "6"),
	(SPELL_LEVEL_7, "7"),
	(SPELL_LEVEL_8, "8"),
	(SPELL_LEVEL_9, "9"),
)

ABJURATION    = "AB"
CONJURATION   = "CO"
DIVINATION    = "DI"
ENCHANTMENT   = "EN"
EVOCATION     = "EV"
ILLUSION      = "IL"
NECROMANCY    = "NE"
TRANSMUTATION = "TR"

SCHOOLS_CHOICES = (
	(ABJURATION, "Abjuration"),
	(CONJURATION, "Conjuration"),
	(DIVINATION, "Divination"),
	(ENCHANTMENT, "Enchantment"),
	(EVOCATION, "Evocation"),
	(ILLUSION, "Illusion"),
	(NECROMANCY, "Necromancy"),
	(TRANSMUTATION, "Transmutation"),
)

MELEE  = "M"
RANGED = "R"
ATTACK_TYPE_CHOICES = (
	("", "None"),
	(MELEE, "Melee"),
	(RANGED, "Ranged"),
)

STRENGTH     = "ST"
DEXTERITY    = "DE"
CONSTITUTION = "CO"
INTELLIGENCE = "IN"
WISDOM       = "WI"
CHARISMA     = "CH"

STAT_CHOICES = (
	("", "None"),
	(STRENGTH, "Strength"),
	(DEXTERITY, "Dexterity"),
	(CONSTITUTION, "Constitution"),
	(INTELLIGENCE, "Intelligence"),
	(WISDOM, "Wisdom"),
	(CHARISMA, "Charisma"),
)

MELEE_WEAPON           = "MW"
RANGED_WEAPON          = "RW"
MELEE_OR_RANGED_WEAPON = "MR"
MELEE_SPELL            = "MS"
RANGED_SPELL           = "RS"

TYPE_CHOICES = (
	(MELEE_WEAPON, "Melee Weapon Attack"),
	(RANGED_WEAPON, "Ranged Weapon Attack"),
	(MELEE_OR_RANGED_WEAPON, "Melee or Ranged Weapon Attack"),
	(MELEE_SPELL, "Melee Weapon Attack"),
	(RANGED_SPELL, "Ranged Weapon Attack"),
)

ACID        = "AC"
BLUDGEONING = "BL"
COLD        = "CO"
FIRE        = "FI"
FORCE       = "FO"
LIGHTNING   = "LI"
NECROTIC    = "NE"
PIERCING    = "PI"
POISON      = "PO"
PSYCHIC     = "PS"
RADIANT     = "RA"
SLASHING    = "SL"
THUNDER     = "TH"

DAMAGE_TYPE_CHOICES = (
	("", "None"),
	(ACID, "Acid"),
	(BLUDGEONING, "Bludgeoning"),
	(COLD, "Cold"),
	(FIRE, "Fire"),
	(FORCE, "Force"),
	(LIGHTNING, "Lightning"),
	(NECROTIC, "Necrotic"),
	(PIERCING, "Piercing"),
	(POISON, "Poison"),
	(PSYCHIC, "Psychic"),
	(RADIANT, "Radiant"),
	(SLASHING, "Slashing"),
	(THUNDER, "Thunder"),
)

TINY       = 'T'
SMALL      = 'S'
MEDIUM     = 'M'
LARGE      = 'L'
HUGE       = 'H'
GARGANTUAN = 'G'

SIZE_CHOICES = (
	(TINY, "Tiny"),
	(SMALL, "Small"),
	(MEDIUM, "Medium"),
	(LARGE, "Large"),
	(HUGE, "Huge"),
	(GARGANTUAN, "Gargantuan"),
)

ABERRATION  = "AB"
BEAST       = "BE"
CELESTIAL   = "CE"
CONSTRUCT   = "CO"
DRAGON      = "DR"
ELEMENTAL   = "EL"
FEY         = "FE"
FIEND       = "FI"
GIANT       = "GI"
HUMANOID    = "HU"
MONSTROSITY = "MO"
OOZE        = "OO"
PLANT       = "PL"
UNDEAD      = "UN"

TYPE_CHOICES = (
	("", "None"),
	(ABERRATION, "Aberration"),
	(BEAST, "Beast"),
	(CELESTIAL, "Celestial"),
	(CONSTRUCT, "Construct"),
	(DRAGON, "Dragon"),
	(ELEMENTAL, "Elemental"),
	(FEY, "Fey"),
	(FIEND, "Fiend"),
	(GIANT, "Giant"),
	(HUMANOID, "Humanoid"),
	(MONSTROSITY, "Monstrosity"),
	(OOZE, "Ooze"),
	(PLANT, "Plant"),
	(UNDEAD, "Undead"),
)

UNALIGNED       = "UN"
LAWFUL_GOOD     = "LG"
NEUTRAL_GOOD    = "NG"
CHAOTIC_GOOD    = "CG"
LAWFUL_NEUTRAL  = "LN"
TRUE_NEUTRAL    = "TN"
CHAOTIC_NEUTRAL = "CN"
LAWFUL_EVIL     = "LE"
NEUTRAL_EVIL    = "NE"
CHAOTIC_EVIL    = "CE"
FIRE            = "FI"
EARTH           = "EA"
AIR             = "AI"
WATER           = "WA"
VOID            = "VO"

ALIGNMENT_CHOICES = (
	(UNALIGNED, "Unaligned"),
	(LAWFUL_GOOD, "Lawful Good"),
	(NEUTRAL_GOOD, "Neutral Good"),
	(CHAOTIC_GOOD, "Chaotic Good"),
	(LAWFUL_NEUTRAL, "Lawful Neutral"),
	(TRUE_NEUTRAL, "True Neutral"),
	(CHAOTIC_NEUTRAL, "Chaotic Neutral"),
	(LAWFUL_EVIL, "Lawful Evil"),
	(NEUTRAL_EVIL, "Neutral Evil"),
	(CHAOTIC_EVIL, "Chaotic Evil"),
	(FIRE, "Fire"),
	(EARTH, "Earth"),
	(AIR, "Air"),
	(WATER, "Water"),
	(VOID, "Void"),
)

ACROBATICS      = "AC"
ANIMAL_HANDLING = "AN"
ARCANA          = "AR"
ATHLETICS       = "AT"
DECEPTION       = "DE"
HISTORY         = "HI"
INSIGHT         = "IS"
INTIMIDATION    = "IT"
INVESTIGATION   = "IV"
MEDICINE        = "ME"
NATURE          = "NA"
PERFORMANCE     = "PF"
PERCEPTION      = "PC"
PERSUASION      = "PS"
RELIGION        = "RE"
SLEIGHT_OF_HAND = "SL"
STEALTH         = "ST"
SURVIVAL        = "SU"

SKILL_CHOICES = (
	(ACROBATICS, "Acrobatics"),
	(ANIMAL_HANDLING, "Animal Handling"),
	(ARCANA, "Arcana"),
	(ATHLETICS, "Athletics"),
	(DECEPTION, "Deception"),
	(HISTORY, "History"),
	(INSIGHT, "Insight"),
	(INTIMIDATION, "Intimidation"),
	(INVESTIGATION, "Investigation"),
	(MEDICINE, "Medicine"),
	(NATURE, "Nature"),
	(PERFORMANCE, "Performance"),
	(PERCEPTION, "Perception"),
	(PERSUASION, "Persuasion"),
	(RELIGION, "Religion"),
	(SLEIGHT_OF_HAND, "Sleight of Hand"),
	(STEALTH, "Stealth"),
	(SURVIVAL, "Survival"),
)

PROFICIENT         = 1
EXPERTISE          = 2
JACK_OF_ALL_TRADES = 3

SKILL_PROFICIENCY_CHOICES = (
	(0, "None"),
	(PROFICIENT, "Proficient"),
	(EXPERTISE, "Expertise"),
	(JACK_OF_ALL_TRADES, "Jack of All Trades"),
)

TOOL_PROFICIENCY_CHOICES = (
	(PROFICIENT, "Proficient"),
	(EXPERTISE, "Expertise"),
	(JACK_OF_ALL_TRADES, "Jack of All Trades"),
)

LANGUAGE = "L"
ARMOR    = "A"
WEAPON   = "W"
OTHER    = "O"

PROFICIENCY_TYPE_CHOICES = (
	(LANGUAGE, "Language"),
	(ARMOR, "Armor"),
	(WEAPON, "Weapon"),
	(OTHER, "Other"),
)

class PositiveSmallIntegerRangeField(models.PositiveSmallIntegerField):
	def __init__(self, verbose_name=None, name=None, min_value=0, max_value=None, **kwargs):
		self.min_value, self.max_value = min_value, max_value
		models.PositiveSmallIntegerField.__init__(self, verbose_name, name, **kwargs)

	def formfield(self, **kwargs):
		defaults = {
			"min_value": self.min_value,
			"max_value": self.max_value,
		}
		defaults.update(kwargs)
		return super(PositiveSmallIntegerRangeField, self).formfield(**defaults)

class Resource(models.Model):
	name = models.CharField(max_length=64)
	total = models.PositiveSmallIntegerField(default=1)
	left = models.PositiveSmallIntegerField(default=1)

	def use(self):
		if self.left > 0:
			self.left -= 1

	def __str__(self):
		return self.name

	def clean(self):
		if self.left > self.total:
			self.left = self.total

class Item(models.Model):
	name   = models.CharField(max_length=128)
	amount = models.PositiveSmallIntegerField(default = 1)
	weight = models.PositiveSmallIntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

class Money(models.Model):
	cp = models.PositiveSmallIntegerField(default=0)
	sp = models.PositiveSmallIntegerField(default=0)
	ep = models.PositiveSmallIntegerField(default=0)
	gp = models.PositiveSmallIntegerField(default=0)
	pp = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		gold = self.cp / 100 + self.sp / 10 + self.ep / 2 + self.gp + self.pp * 10
		return str(gold)

	@property
	def weight(self):
		return (cp + sp + ep + gp + pp) / 50

class ToolProficiency(models.Model):
	name              = models.CharField(max_length=32, default="")
	proficiency_bonus = models.PositiveSmallIntegerField(choices=TOOL_PROFICIENCY_CHOICES, default=PROFICIENT)
	attribute         = models.CharField(max_length=2, choices=STAT_CHOICES, default=STRENGTH)
	modifier          = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.name

class OtherProficiency(models.Model):
	type        = models.CharField(max_length=1, choices=PROFICIENCY_TYPE_CHOICES, default=LANGUAGE)
	proficiency = models.CharField(max_length=32, default="")

	def __str__(self):
		return self.type

class Senses(models.Model):
	passive_perception = models.PositiveSmallIntegerField(default=10)
	blindsight         = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	darkvision         = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	tremorsense        = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	truesight          = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

class Speed(models.Model):
	speed        = models.PositiveSmallIntegerField(default=30)
	speed_burrow = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	speed_climb  = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	speed_fly    = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	speed_swim   = models.PositiveSmallIntegerField(blank=True, null=True, default=None)
	speed_hover  = models.BooleanField(default=False)

class Skills(models.Model):
	acrobatics      = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	animal_handling = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	arcana          = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	athletics       = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	deception       = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	history         = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	insight         = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	intimidation    = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	investigation   = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	medicine        = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	nature          = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	performance     = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	perception      = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	persuasion      = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	religion        = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	sleight_of_hand = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	stealth         = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)
	survival        = models.PositiveSmallIntegerField(choices=SKILL_PROFICIENCY_CHOICES, default=0)

	def clean(self):
		for attr, value in self.__dict__.items():
			if value > JACK_OF_ALL_TRADES:
				raise ValidationError(_("{} has an invalid value".format(attr)))
		# if self.acrobatics > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("acrobatics has an invalid value"))
		# if self.animal_handling > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("animal_handling has an invalid value"))
		# if self.arcana > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("arcana has an invalid value"))
		# if self.athletics > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("athletics has an invalid value"))
		# if self.deception > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("deception has an invalid value"))
		# if self.history > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("history has an invalid value"))
		# if self.insight > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("insight has an invalid value"))
		# if self.intimidation > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("intimidation has an invalid value"))
		# if self.investigation > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("investigation has an invalid value"))
		# if self.medicine > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("medicine has an invalid value"))
		# if self.nature > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("nature has an invalid value"))
		# if self.performance > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("performance has an invalid value"))
		# if self.perception > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("perception has an invalid value"))
		# if self.persuasion > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("persuasion has an invalid value"))
		# if self.religion > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("religion has an invalid value"))
		# if self.sleight_of_hand > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("sleight_of_hand has an invalid value"))
		# if self.stealth > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("stealth has an invalid value"))
		# if self.survival > JACK_OF_ALL_TRADES:
		# 	raise ValidationError(_("survival has an invalid value"))


class Spell(models.Model):
	name                     = models.CharField(max_length=32)
	level                    = PositiveSmallIntegerRangeField(choices=SPELL_LEVEL_CHOICES, min_value=CANTRIP, max_value=SPELL_LEVEL_9, default=CANTRIP)
	school                   = models.CharField(max_length=2, choices=SCHOOLS_CHOICES, default=ABJURATION)
	casting_time             = models.CharField(max_length=16, default="1 Action")
	range                    = models.CharField(max_length=32, default="30 feet")
	verbal                   = models.BooleanField(default=False)
	somatic                  = models.BooleanField(default=False)
	material                 = models.BooleanField(default=False)
	material_material        = models.CharField(max_length=32, blank=True, default="")
	duration                 = models.CharField(max_length=32, default="Instantaneous")
	description              = models.TextField(blank=True, default="")
	higher_level_description = models.TextField(blank=True, default="")

	attack_type              = models.CharField(max_length=1, choices=ATTACK_TYPE_CHOICES, default="")
	damage                   = models.CharField(max_length=64, default="1d6")
	damage_type              = models.CharField(max_length=2, choices=DAMAGE_TYPE_CHOICES, default="")
	damage_type_other        = models.CharField(max_length=128, blank=True, default="")
	higher_level_dice        = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
	damage2                  = models.CharField(max_length=64, blank=True, default="")
	damage2_type             = models.CharField(max_length=2, choices=DAMAGE_TYPE_CHOICES, default="")
	damage2_type_other       = models.CharField(max_length=128, blank=True, default="")
	higher_level_dice2       = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

	save_ability             = models.CharField(max_length=2, choices=STAT_CHOICES, default="")
	save_success             = models.CharField(max_length=128, blank=True)

	def __str__(self):
		return self.name

	def clean(self):
		if self.material:
			# If it has a material component, the material must be given
			if not self.material_material:
				raise ValidationError(_("The spell requires a material component."))

		if self.attack_type:
			# If the attack_type is given, the damage and damage type must also be given
			if not self.damage:
				raise ValidationError(_("Spell Damage not given."))
			if not self.damage_type and not self.damage_type_other:
				raise ValidationError(_("Spell Damage Type not given."))
		elif self.damage:
			# If the damage property is given, the damage_type must also be given
			if not self.damage_type:
				raise ValidationError(_("Spell Damage Type not given."))
			if self.damage2: # We only care about damage2 if damage is given.
				# If the damage2 is given, the damage2 type must also be given
				if not self.damage2_type and not self.damage2damage2_type_other:
					raise ValidationError(_("Spell Secondary Damage Type not given."))

		if self.higher_level_dice:
			# If the higher_level_dice is given, the damage and damage type must also be given
			if not self.damage:
				raise ValidationError(_("Spell Damage not given."))
			if not self.damage_type and not self.damage_type_other:
				raise ValidationError(_("Spell Damage Type not given."))
			if self.higher_level_dice2:
				# If the higher_level_dice2 is given, the damage2 and damage2 type must also be given
				if not self.damage2:
					raise ValidationError(_("Spell Damage not given."))
				if not self.damage2_type and not self.damage2_type_other:
					raise ValidationError(_("Spell Damage Type not given."))
		if self.save_ability:
			# If it has a save ability, it needs a save success
			if not self.save_success:
				raise ValidationError(_("Spell Save Success not given."))

class Ability(models.Model):
	name        = models.CharField(max_length=32)
	description = models.TextField(blank=True, default="")
	recharge    = models.CharField(max_length=32, default="")

	def __str__(self):
		return self.name

	class Meta:
		abstract = True
		ordering = ["name"]

class Trait(Ability):
	pass # No need for other fields

class Action(Ability):
	type           = models.CharField(
		max_length = 2,
		choices    = TYPE_CHOICES,
		default    = "",
	)
	to_hit       = models.IntegerField(default=0)
	reach        = models.PositiveSmallIntegerField(default=5, blank=True, null=True)
	range        = models.CharField(max_length=7, blank=True, default="")
	targets      = models.PositiveSmallIntegerField(default=1)
	damage       = models.CharField(max_length=16, default="1d6")
	damage_type  = models.CharField(max_length=2, choices=DAMAGE_TYPE_CHOICES, default=SLASHING)
	crit         = models.CharField(max_length=16, blank=True, default="")
	damage2      = models.CharField(max_length=16, blank=True, default="")
	damage2_type = models.CharField(max_length=2, choices=DAMAGE_TYPE_CHOICES, default=SLASHING)
	crit2        = models.CharField(max_length=16, blank=True, default="")
	save         = models.CharField(max_length=2, choices=STAT_CHOICES, default="")
	save_dc      = models.PositiveSmallIntegerField(blank=True, default="")
	save_success = models.CharField(max_length=128, blank=True, default="")
	description  = models.TextField(blank=True, default="")

class Creature(models.Model):
	name              = models.CharField(max_length=64)
	size              = models.CharField(max_length=1, choices=SIZE_CHOICES, default=MEDIUM)
	type              = models.CharField(max_length=2, choices=TYPE_CHOICES, default=HUMANOID)
	alignment         = models.CharField(max_length=2, choices=ALIGNMENT_CHOICES, default=UNALIGNED)
	ac                = models.PositiveSmallIntegerField(default=10)
	ac_type           = models.CharField(max_length=32, blank=True, default="")
	initiative        = models.SmallIntegerField(default=0)
	hp                = models.PositiveSmallIntegerField(default=0)
	speed             = models.OneToOneField(Speed, on_delete=models.CASCADE)

	strength          = models.PositiveSmallIntegerField(default=10)
	dexterity         = models.PositiveSmallIntegerField(default=10)
	constitution      = models.PositiveSmallIntegerField(default=10)
	intelligence      = models.PositiveSmallIntegerField(default=10)
	wisdom            = models.PositiveSmallIntegerField(default=10)
	charisma          = models.PositiveSmallIntegerField(default=10)

	strength_save     = models.BooleanField(default=False)
	dexterity_save    = models.BooleanField(default=False)
	constitution_save = models.BooleanField(default=False)
	intelligence_save = models.BooleanField(default=False)
	wisdom_save       = models.BooleanField(default=False)
	charisma_save     = models.BooleanField(default=False)

	skills            = models.OneToOneField(Skills, on_delete=models.CASCADE, null=True, blank=True)
	senses            = models.OneToOneField(Senses, on_delete=models.CASCADE, null=True, blank=True)
	traits            = models.ForeignKey(Trait, on_delete=models.CASCADE, blank=True)
	actions           = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True)
	spells            = models.ForeignKey(Spell, on_delete=models.CASCADE, blank=True)

	@property
	def strength_mod(self):
		return int(math.floor((strength - 10) / 2))

	@property
	def dexterity_mod(self):
		return int(math.floor((dexterity - 10) / 2))

	@property
	def constitution_mod(self):
		return int(math.floor((constitution - 10) / 2))

	@property
	def intelligence_mod(self):
		return int(math.floor((intelligence - 10) / 2))

	@property
	def wisdom_mod(self):
		return int(math.floor((wisdom - 10) / 2))

	@property
	def charisma_mod(self):
		return int(math.floor((charisma - 10) / 2))

	def __str__(self):
		return self.name

	def clean(self):
		if not re.match(DICE_REGEX, self.hp_dice, re.IGNORECASE):
			raise ValidationError(_("HP Dice is invalid."))

	class Meta:
		abstract = True
		ordering = ["name"]

class Monster(Creature):
	hp_dice                  = models.CharField(max_length=16)
	challenge_rating         = models.CharField(max_length=3, choices=CHALLENGE_RATING_CHOICES, default="0")
	@property
	def proficiency_bonus(self):
		CR                   = dict(CHALLENGE_RATING_CHOICES)
		return int(math.floor((CR[self.challenge_rating] + 7) / 5))

	@property
	def experience(self):
		return CHALLENGE_RATING_EXPERIENCE[self.challenge_rating]

	damage_vulnerabilities   = models.CharField(max_length=128, blank=True, default="")
	damage_resistances       = models.CharField(max_length=128, blank=True, default="")
	damage_immunities        = models.CharField(max_length=128, blank=True, default="")
	condition_immunities     = models.CharField(max_length=128, blank=True, default="")

	legendary_actions_amount = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
	legendary_actions        = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, related_name="legendary_actions")


class PlayerCharacter(Creature):
	owner                          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	current_hp                     = models.PositiveSmallIntegerField(default=0)
	temp_hp                        = models.PositiveSmallIntegerField(default=0)
	hit_dice_d6                    = models.PositiveSmallIntegerField(default=0)
	hit_dice_d8                    = models.PositiveSmallIntegerField(default=0)
	hit_dice_d10                   = models.PositiveSmallIntegerField(default=0)
	hit_dice_d12                   = models.PositiveSmallIntegerField(default=0)
	hit_dice_d6_left               = models.PositiveSmallIntegerField(default=0)
	hit_dice_d8_left               = models.PositiveSmallIntegerField(default=0)
	hit_dice_d10_left              = models.PositiveSmallIntegerField(default=0)
	hit_dice_d12_left              = models.PositiveSmallIntegerField(default=0)

	death_save_success_1           = models.BooleanField(default=False)
	death_save_success_2           = models.BooleanField(default=False)
	death_save_success_3           = models.BooleanField(default=False)
	death_save_failure_1           = models.BooleanField(default=False)
	death_save_failure_2           = models.BooleanField(default=False)
	death_save_failure_3           = models.BooleanField(default=False)

	class_and_level                = models.CharField(max_length=128, default="")
	level                          = models.PositiveSmallIntegerField(default=1)
	experience                     = models.PositiveSmallIntegerField(default=0)

	@property
	def next_level(self):
		if level > 20:
			return EXPERIENCE_ARRAY[-1] # If level for some reason is above 20, return whatever the last thing in the array is
		return EXPERIENCE_ARRAY[self.level]

	@property
	def proficiency_bonus(self):
		return int(math.floor((self.level + 7) / 5))

	inspiration                    = models.BooleanField(default=False)
	tool_proficiencies             = models.ForeignKey(ToolProficiency, on_delete=models.CASCADE, blank=True, related_name="tool_proficiencies")
	proficiencies                  = models.ForeignKey(OtherProficiency, on_delete=models.CASCADE, blank=True, related_name="proficiencies")

	resources                      = models.ForeignKey(Resource, on_delete=models.CASCADE, blank=True, related_name="resources")

	inventory                      = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, related_name="items")
	money                          = models.OneToOneField(Money, on_delete=models.CASCADE, blank=True, related_name="money")

	spellcaster                    = models.BooleanField(default=False)
	spellcasting_ability           = models.CharField(max_length=2, choices=STAT_CHOICES, default="")
	spell_save_dc                  = models.PositiveSmallIntegerField(default=8)
	spell_attack_bonus             = models.PositiveSmallIntegerField(default=0)

	spell_slot_1                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_1_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_2                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_2_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_3                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_3_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_4                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_4_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_5                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_5_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_6                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_6_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_7                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_7_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_8                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_8_left              = models.PositiveSmallIntegerField(default=0)
	spell_slot_9                   = models.PositiveSmallIntegerField(default=0)
	spell_slot_9_left              = models.PositiveSmallIntegerField(default=0)

	background                     = models.CharField(max_length=32, blank=True, default="")
	personality_trait              = models.TextField(blank=True, default="")
	ideals                         = models.TextField(blank=True, default="")
	bonds                          = models.TextField(blank=True, default="")
	flaws                          = models.TextField(blank=True, default="")

	race                           = models.CharField(max_length=32, blank=True, default="")
	age                            = models.CharField(max_length=32, blank=True, default="")
	height                         = models.CharField(max_length=32, blank=True, default="")
	weight                         = models.CharField(max_length=32, blank=True, default="")
	eyes                           = models.CharField(max_length=32, blank=True, default="")
	skin                           = models.CharField(max_length=32, blank=True, default="")
	hair                           = models.CharField(max_length=32, blank=True, default="")

	character_appearance           = models.TextField(blank=True, default="")
	allies_and_organizations       = models.TextField(blank=True, default="")
	backstory                      = models.TextField(blank=True, default="")
	additional_features_and_traits = models.TextField(blank=True, default="")
	treasure                       = models.TextField(blank=True, default="")
