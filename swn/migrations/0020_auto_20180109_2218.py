# Generated by Django 2.0 on 2018-01-09 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0019_auto_20180109_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('asset_attribute', models.CharField(max_length=128)),
                ('hp', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('tl', models.IntegerField()),
                ('asset_type', models.CharField(max_length=32)),
                ('attack', models.CharField(max_length=16)),
                ('counterattack', models.CharField(max_length=16)),
                ('special', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('faction_type', models.CharField(max_length=128)),
                ('force', models.IntegerField()),
                ('cunning', models.IntegerField()),
                ('wealth', models.IntegerField()),
                ('current_hp', models.IntegerField()),
                ('max_hp', models.IntegerField()),
                ('income', models.IntegerField()),
                ('faccreds', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('pc_reputation', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Faction_Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_hp', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=32)),
                ('asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Asset')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Planet')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='Faction_Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faction_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='goal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Faction_Goal'),
        ),
        migrations.AddField(
            model_name='faction',
            name='homeworld',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swn.Planet'),
        ),
        migrations.AddField(
            model_name='faction',
            name='tags',
            field=models.ManyToManyField(to='swn.Faction_Tag'),
        ),
    ]
