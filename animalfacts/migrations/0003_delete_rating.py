# Generated by Django 4.1.1 on 2022-10-04 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalfacts', '0002_animalfact_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]