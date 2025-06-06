# Generated by Django 5.2.1 on 2025-05-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerimage',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(upload_to='main/workers'),
        ),
        migrations.AlterField(
            model_name='workerimage',
            name='work_picture',
            field=models.ImageField(upload_to='main/workers_work'),
        ),
    ]
