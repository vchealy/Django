# Generated by Django 3.1.1 on 2020-09-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_auto_20200915_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagues',
            name='league_id',
            field=models.IntegerField(default=20, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leagues',
            name='league_logo',
            field=models.URLField(blank=True, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='leagues',
            name='league_season',
            field=models.CharField(blank=True, max_length=20, verbose_name='Season'),
        ),
    ]
