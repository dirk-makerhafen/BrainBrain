# Generated by Django 2.0.1 on 2018-03-11 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0027_individual_fitnessevalcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='fitnessevalcount',
        ),
    ]