# Generated by Django 4.0.4 on 2022-07-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameTimeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='event',
            name='fecha',
            field=models.CharField(max_length=255),
        ),
    ]