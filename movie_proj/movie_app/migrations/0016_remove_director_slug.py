# Generated by Django 4.2.5 on 2023-09-20 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_director_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='slug',
        ),
    ]
