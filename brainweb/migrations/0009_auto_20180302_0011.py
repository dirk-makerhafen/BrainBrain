# Generated by Django 2.0.1 on 2018-03-02 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0008_auto_20180302_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='codetokens',
            new_name='code',
        ),
    ]