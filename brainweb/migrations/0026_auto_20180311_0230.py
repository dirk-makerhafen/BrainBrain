# Generated by Django 2.0.1 on 2018-03-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0025_referencefunction_step_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='min_fitness_evaluation_per_individual',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='problem',
            name='default_min_fitness_evaluation_per_individual',
            field=models.IntegerField(default=-1),
        ),
    ]
