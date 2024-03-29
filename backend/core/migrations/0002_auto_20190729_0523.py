# Generated by Django 2.2.2 on 2019-07-29 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='areacode.District'),
        ),
        migrations.AlterField(
            model_name='user',
            name='regency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regencies', to='areacode.Regency'),
        ),
        migrations.AlterField(
            model_name='user',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='areacode.Village'),
        ),
    ]
