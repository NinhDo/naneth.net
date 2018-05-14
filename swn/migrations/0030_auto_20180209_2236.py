# Generated by Django 2.0 on 2018-02-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0029_auto_20180209_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_notes', models.TextField(blank='True', default='')),
                ('gm_notes', models.TextField(blank='True', default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='aliennotes',
            name='alien',
        ),
        migrations.RemoveField(
            model_name='corporationnotes',
            name='Corporation',
        ),
        migrations.RemoveField(
            model_name='factionnotes',
            name='faction',
        ),
        migrations.RemoveField(
            model_name='heresynotes',
            name='heresy',
        ),
        migrations.RemoveField(
            model_name='npcnotes',
            name='npc',
        ),
        migrations.RemoveField(
            model_name='politicalgroupnotes',
            name='political_group',
        ),
        migrations.RemoveField(
            model_name='religionnotes',
            name='religion',
        ),
        migrations.RemoveField(
            model_name='systemnotes',
            name='system',
        ),
        migrations.RemoveField(
            model_name='npc',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='system',
            name='notes',
        ),
        migrations.DeleteModel(
            name='AlienNotes',
        ),
        migrations.DeleteModel(
            name='CorporationNotes',
        ),
        migrations.DeleteModel(
            name='FactionNotes',
        ),
        migrations.DeleteModel(
            name='HeresyNotes',
        ),
        migrations.DeleteModel(
            name='NPCNotes',
        ),
        migrations.DeleteModel(
            name='PoliticalGroupNotes',
        ),
        migrations.DeleteModel(
            name='ReligionNotes',
        ),
        migrations.DeleteModel(
            name='SystemNotes',
        ),
    ]