# Generated by Django 2.0 on 2018-01-09 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0021_auto_20180109_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Faction_Goal'),
        ),
        migrations.AlterField(
            model_name='faction',
            name='homeworld',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Planet'),
        ),
    ]
