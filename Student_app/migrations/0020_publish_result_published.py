# Generated by Django 5.0.6 on 2024-07-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0019_publish_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish_result',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
