# Generated by Django 2.2.2 on 2019-07-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goverment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepemerintahan',
            name='jabatan',
        ),
        migrations.RemoveField(
            model_name='profilepemerintahan',
            name='kelembagaan',
        ),
    ]