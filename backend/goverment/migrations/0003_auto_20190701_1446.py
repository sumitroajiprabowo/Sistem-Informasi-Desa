# Generated by Django 2.2.2 on 2019-07-01 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goverment', '0002_auto_20190701_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jabatan',
            options={'ordering': ['kelembagaan'], 'verbose_name_plural': 'jabatan'},
        ),
    ]