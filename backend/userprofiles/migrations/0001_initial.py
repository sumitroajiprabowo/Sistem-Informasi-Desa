# Generated by Django 2.2.2 on 2019-07-22 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='alamat')),
                ('headman', models.CharField(max_length=50, verbose_name='kades')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('zip_code', models.CharField(blank=True, max_length=5, verbose_name='kodepos')),
                ('bio', models.CharField(blank=True, max_length=50, null=True, verbose_name='biografi')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='ProfileStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_content', models.CharField(max_length=240)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
            ],
            options={
                'verbose_name_plural': 'statuses',
                'db_table': 'profiles_status',
            },
        ),
    ]
