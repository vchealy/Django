# Generated by Django 3.1.1 on 2020-09-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_remove_countries_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='country_logo',
            field=models.URLField(max_length=150, null=True),
        ),
    ]
