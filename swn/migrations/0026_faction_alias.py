# Generated by Django 2.0 on 2018-01-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0025_faction_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='alias',
            field=models.CharField(default='alias', max_length=128),
            preserve_default=False,
        ),
    ]