# Generated by Django 3.1.1 on 2020-09-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_remove_teams_date_now'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team_id',
            new_name='team_key',
        ),
        migrations.AddField(
            model_name='teams',
            name='team_badge',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
