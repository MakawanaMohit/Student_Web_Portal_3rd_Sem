# Generated by Django 5.0.6 on 2024-07-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0022_alter_publish_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish_result',
            name='id',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]
