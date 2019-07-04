# Generated by Django 2.2.2 on 2019-07-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Kecamatan',
                'db_table': 'area_districts',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Provinsi',
                'db_table': 'area_provinces',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areacode.District')),
            ],
            options={
                'verbose_name_plural': 'Desa',
                'db_table': 'area_villages',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areacode.Province')),
            ],
            options={
                'verbose_name_plural': 'Kabupaten',
                'db_table': 'area_regencies',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='district',
            name='regency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areacode.Regency'),
        ),
    ]
