# Generated by Django 4.2.5 on 2023-09-30 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
