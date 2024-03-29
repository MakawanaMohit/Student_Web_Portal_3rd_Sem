# Generated by Django 4.2.5 on 2023-12-23 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_rename_profile_pic_user_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_Records',
            fields=[
                ('fac_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(default='Enter your email here', max_length=254)),
                ('fac_name', models.CharField(max_length=25)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.faculty')),
            ],
        ),
    ]
