# Generated by Django 2.0 on 2018-02-09 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0030_auto_20180209_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='alien',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='corporation',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='faction',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='heresy',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='npc',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='planet',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='politicalgroup',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='religion',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
        migrations.AddField(
            model_name='system',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.Notes'),
        ),
    ]