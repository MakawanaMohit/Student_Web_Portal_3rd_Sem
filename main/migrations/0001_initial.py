# Generated by Django 4.2.5 on 2023-09-25 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0004_alter_faculty_records_fac_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='GtuExam',
            fields=[
                ('sub_code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('sub_sem', models.IntegerField(default=0)),
                ('sub_academic_term', models.CharField(max_length=5)),
                ('sub_session', models.CharField(max_length=6)),
                ('sub_pdf', models.FileField(upload_to='home/pdfs/exam')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Syllabus',
            fields=[
                ('sub_name', models.CharField(max_length=100)),
                ('sub_code', models.IntegerField(primary_key=True, serialize=False)),
                ('sub_theory_mid1', models.IntegerField(default=0)),
                ('sub_theory_mid2', models.IntegerField(default=0)),
                ('sub_theory_micro', models.IntegerField(default=0)),
                ('sub_theory_ESE', models.IntegerField(default=0)),
                ('sub_prctical_PA', models.IntegerField(default=0)),
                ('sub_prctical_ESE', models.IntegerField(default=0)),
                ('sub_sem', models.IntegerField(default=0)),
                ('sub_credit', models.IntegerField(default=0)),
                ('sub_academic_term', models.CharField(max_length=5)),
                ('sub_pdf', models.FileField(upload_to='home/images/')),
                ('Assigned_Sub_Faculty', models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty_records')),
            ],
        ),
    ]
