# Generated by Django 2.0.5 on 2018-09-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0002_auto_20180910_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='damage',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='spell',
            name='material_material',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='spell',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='spell',
            name='save_success',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]