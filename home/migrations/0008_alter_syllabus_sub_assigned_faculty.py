# Generated by Django 4.2.5 on 2023-09-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_syllabus_sub_assigned_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='sub_assigned_faculty',
            field=models.CharField(max_length=100),
        ),
    ]
