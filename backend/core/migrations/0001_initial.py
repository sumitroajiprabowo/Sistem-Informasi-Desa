# Generated by Django 2.2.2 on 2019-07-22 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('areacode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('username', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='areacode.District')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='areacode.Province')),
                ('regency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regencies', to='areacode.Regency')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('village', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='areacode.Village')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
