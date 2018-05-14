# Generated by Django 2.0 on 2018-02-09 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0028_faction_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlienNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='CorporationNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='FactionNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='HeresyNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='NPCNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.NPC')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalGroupNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='ReligionNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.CreateModel(
            name='SystemNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.System')),
            ],
        ),
        migrations.RemoveField(
            model_name='alien',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='corporation',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='faction',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='heresy',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='planet',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='politicalgroup',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='religion',
            name='notes',
        ),
        migrations.AddField(
            model_name='religionnotes',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Religion'),
        ),
        migrations.AddField(
            model_name='politicalgroupnotes',
            name='political_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.PoliticalGroup'),
        ),
        migrations.AddField(
            model_name='heresynotes',
            name='heresy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Heresy'),
        ),
        migrations.AddField(
            model_name='factionnotes',
            name='faction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Faction'),
        ),
        migrations.AddField(
            model_name='corporationnotes',
            name='Corporation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Corporation'),
        ),
        migrations.AddField(
            model_name='aliennotes',
            name='alien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swn.Alien'),
        ),
    ]