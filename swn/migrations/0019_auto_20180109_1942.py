# Generated by Django 2.0 on 2018-01-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0018_auto_20171230_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='alias',
            field=models.CharField(default='alias', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system',
            name='alias',
            field=models.CharField(default='alias', max_length=128),
            preserve_default=False,
        ),
    ]
