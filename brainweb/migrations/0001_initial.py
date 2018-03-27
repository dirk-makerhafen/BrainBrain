# Generated by Django 2.0.1 on 2018-03-01 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
        ),
        migrations.AddField(
            model_name='population',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='populations', to='brainweb.Problem'),
        ),
        migrations.AddField(
            model_name='individual',
            name='population',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='individual', to='brainweb.Population'),
        ),
    ]
