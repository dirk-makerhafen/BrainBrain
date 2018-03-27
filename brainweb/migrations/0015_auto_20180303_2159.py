# Generated by Django 2.0.1 on 2018-03-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0014_auto_20180303_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='default_max_generations',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='problem',
            name='default_max_individuals',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='problem',
            name='default_max_populationsize',
            field=models.IntegerField(default=100),
        ),
    ]
