# Generated by Django 4.2.5 on 2023-12-23 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_name', models.CharField(default='', max_length=50)),
                ('stu_enroll', models.CharField(default=0, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('stu_sem', models.IntegerField()),
                ('stu_DOB', models.DateField(default=datetime.date(2007, 1, 1))),
                ('stu_branch', models.CharField(max_length=110)),
                ('stu_branch_code', models.CharField(default='16', max_length=2)),
                ('stu_mobile_num', models.CharField(max_length=10)),
                ('stu_parents_mobile_num', models.CharField(max_length=10)),
                ('stu_address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Marks',
            fields=[
                ('id', models.CharField(default='hello', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('stu_enroll', models.CharField(default='enrollmentno', max_length=12)),
                ('stu_sem', models.IntegerField(default=5)),
                ('stu_term', models.CharField(default='tern', max_length=5)),
                ('stu_name', models.CharField(default='name', max_length=50)),
                ('sub_name', models.CharField(default='thisissubjectname', max_length=50)),
                ('stu_branch_code', models.CharField(default='16', max_length=2)),
                ('stu_sub_code', models.IntegerField(default=0)),
                ('session', models.CharField(choices=[('WINTER', 'Winter'), ('SUMMER', 'Summer')], default='SUMMER', max_length=50)),
                ('stu_theory_ESE', models.IntegerField(default=0)),
                ('stu_theory_PA', models.IntegerField(default=0)),
                ('stu_practical_ESE', models.IntegerField(default=0)),
                ('stu_practical_PA', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='upload_from_xlsx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_description', models.CharField(default='uploaded in', max_length=250)),
                ('model_name', models.CharField(choices=[('STUDENT', 'Student'), ('STUDENTMARKS', 'StudentMarks')], max_length=50)),
                ('xlsx_file', models.FileField(upload_to='student/xlsx')),
            ],
        ),
    ]