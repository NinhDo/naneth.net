# Generated by Django 2.0 on 2018-01-26 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0026_faction_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='notes',
        ),
    ]
