# Generated by Django 2.0.1 on 2018-03-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0003_auto_20180301_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='fitness',
            field=models.FloatField(blank=True, default=None),
        ),
    ]
