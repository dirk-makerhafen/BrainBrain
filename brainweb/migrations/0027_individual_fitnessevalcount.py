# Generated by Django 2.0.1 on 2018-03-11 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0026_auto_20180311_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='fitnessevalcount',
            field=models.FloatField(default=0),
        ),
    ]