# Generated by Django 3.1.1 on 2020-09-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_teams_league_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='country_id',
            field=models.IntegerField(default=90, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='league_id',
            field=models.IntegerField(blank=True, default=321),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_badge',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='team_key',
            field=models.IntegerField(default=0),
        ),
    ]
