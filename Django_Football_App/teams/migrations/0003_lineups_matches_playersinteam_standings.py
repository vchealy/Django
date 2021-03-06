# Generated by Django 3.1.1 on 2020-09-14 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200909_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineUps',
            fields=[
                ('teams_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teams')),
            ],
            bases=('teams.teams',),
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('teams_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teams')),
            ],
            bases=('teams.teams',),
        ),
        migrations.CreateModel(
            name='PlayersinTeam',
            fields=[
                ('teams_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teams')),
            ],
            bases=('teams.teams',),
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('teams_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.teams')),
            ],
            bases=('teams.teams',),
        ),
    ]
