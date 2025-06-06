# Generated by Django 5.2.1 on 2025-05-27 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=5000)),
                ('price_m', models.IntegerField()),
                ('image', models.ImageField(upload_to='main/fabrics/')),
            ],
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=5000)),
                ('price_m', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='main/nets/')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='workers')),
            ],
        ),
        migrations.CreateModel(
            name='Rolet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=5000)),
                ('price_m', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='main/rolets/')),
                ('fabric', models.ManyToManyField(to='main.fabric')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_picture', models.ImageField(upload_to='workers_work')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worker')),
            ],
        ),
    ]
