# Generated by Django 2.0 on 2017-12-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0002_auto_20171227_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alien',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='heresy',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='npc',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='adventures_prepared',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='capital_and_government',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='cultural_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='party_activities_on_this_world',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='politicalgroup',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='religion',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='system',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]