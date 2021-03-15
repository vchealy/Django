# Generated by Django 3.1.1 on 2020-09-15 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0009_auto_20200915_1519'),
        ('teams', '0010_auto_20200915_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='league_id',
        ),
        migrations.AddField(
            model_name='teams',
            name='league_team',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='leagues.leagues', verbose_name='League'),
        ),
    ]