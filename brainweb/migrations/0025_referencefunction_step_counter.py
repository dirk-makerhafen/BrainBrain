# Generated by Django 2.0.1 on 2018-03-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0024_auto_20180310_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencefunction',
            name='step_counter',
            field=models.FloatField(default=0),
        ),
    ]