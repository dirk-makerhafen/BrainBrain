# Generated by Django 2.0.1 on 2018-03-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0031_auto_20180314_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencefunction',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]