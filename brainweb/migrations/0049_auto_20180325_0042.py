# Generated by Django 2.0.1 on 2018-03-25 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0048_auto_20180325_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='population',
            old_name='max_code_length',
            new_name='evolved_max_code_length',
        ),
    ]
