# Generated by Django 2.0.1 on 2018-03-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brainweb', '0029_auto_20180312_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='code',
            field=models.CharField(default='..........', max_length=20000),
        ),
        migrations.AlterField(
            model_name='individual',
            name='code_length',
            field=models.FloatField(default=10),
        ),
        migrations.AlterField(
            model_name='population',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='populations', to='brainweb.Problem'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='default_max_code_length',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='problem',
            name='default_min_code_length',
            field=models.IntegerField(default=20),
        ),
    ]