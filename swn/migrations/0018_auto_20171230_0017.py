# Generated by Django 2.0 on 2017-12-29 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swn', '0017_auto_20171229_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Corporation',
        ),
        migrations.RenameField(
            model_name='politicalgroup',
            old_name='key_issues',
            new_name='key_issue1',
        ),
        migrations.AddField(
            model_name='politicalgroup',
            name='key_issue2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='swn.QuickPoliticalIssues'),
            preserve_default=False,
        ),
    ]
