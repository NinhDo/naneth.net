# Generated by Django 2.0 on 2018-02-16 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0032_auto_20180216_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='last_editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
