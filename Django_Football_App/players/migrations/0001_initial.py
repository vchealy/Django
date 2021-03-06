# Generated by Django 3.1.1 on 2020-09-15 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0011_auto_20200915_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_key', models.IntegerField(default=0, verbose_name='ID')),
                ('player_name', models.CharField(default=None, max_length=30, verbose_name='Name')),
                ('player_number', models.IntegerField(blank=True, default=0, verbose_name='shirt #')),
                ('player_country', models.CharField(blank=True, default=None, max_length=20, verbose_name='Country of Origin')),
                ('player_type', models.CharField(blank=True, default=None, max_length=15, verbose_name='Position')),
                ('player_team', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='teams.teams', verbose_name='Team')),
            ],
            options={
                'verbose_name_plural': 'players',
            },
        ),
    ]
