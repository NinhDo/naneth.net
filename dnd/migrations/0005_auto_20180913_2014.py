# Generated by Django 2.0.5 on 2018-09-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0004_auto_20180913_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercharacter',
            name='spellcasting_ability',
            field=models.CharField(blank=True, choices=[('', 'None'), ('ST', 'Strength'), ('DE', 'Dexterity'), ('CO', 'Constitution'), ('IN', 'Intelligence'), ('WI', 'Wisdom'), ('CH', 'Charisma')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='spell',
            name='attack_type',
            field=models.CharField(blank=True, choices=[('', 'None'), ('M', 'Melee'), ('R', 'Ranged')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='spell',
            name='damage2_type',
            field=models.CharField(blank=True, choices=[('', 'None'), ('AC', 'Acid'), ('BL', 'Bludgeoning'), ('CO', 'Cold'), ('FI', 'Fire'), ('FO', 'Force'), ('LI', 'Lightning'), ('NE', 'Necrotic'), ('PI', 'Piercing'), ('PO', 'Poison'), ('PS', 'Psychic'), ('RA', 'Radiant'), ('SL', 'Slashing'), ('TH', 'Thunder')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='spell',
            name='damage_type',
            field=models.CharField(blank=True, choices=[('', 'None'), ('AC', 'Acid'), ('BL', 'Bludgeoning'), ('CO', 'Cold'), ('FI', 'Fire'), ('FO', 'Force'), ('LI', 'Lightning'), ('NE', 'Necrotic'), ('PI', 'Piercing'), ('PO', 'Poison'), ('PS', 'Psychic'), ('RA', 'Radiant'), ('SL', 'Slashing'), ('TH', 'Thunder')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='spell',
            name='save_ability',
            field=models.CharField(blank=True, choices=[('', 'None'), ('ST', 'Strength'), ('DE', 'Dexterity'), ('CO', 'Constitution'), ('IN', 'Intelligence'), ('WI', 'Wisdom'), ('CH', 'Charisma')], default='', max_length=2),
        ),
    ]