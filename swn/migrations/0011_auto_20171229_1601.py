# Generated by Django 2.0 on 2017-12-29 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0010_auto_20171229_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='tag1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swn.WorldTag'),
        ),
        migrations.AddField(
            model_name='planet',
            name='tag2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='swn.WorldTag'),
        ),
    ]
