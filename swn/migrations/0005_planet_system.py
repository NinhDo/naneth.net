# Generated by Django 2.0 on 2017-12-27 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0004_auto_20171227_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='swn.System'),
            preserve_default=False,
        ),
    ]
