# Generated by Django 2.0.1 on 2018-03-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0033_auto_20180314_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='peer',
            name='supernode',
            field=models.BooleanField(default=False),
        ),
    ]
