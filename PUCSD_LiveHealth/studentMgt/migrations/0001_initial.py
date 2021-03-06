# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('attendance_data', models.TextField()),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Course_Class',
            fields=[
                ('class_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('strength', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='studentMgt.Course')),
            ],
            options={
                'db_table': 'couse_class',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.IntegerField()),
                ('marks_out_of', models.IntegerField()),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='studentMgt.Exam')),
            ],
            options={
                'db_table': 'marks',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('contact', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
        migrations.CreateModel(
            name='School_user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('is_active', models.BooleanField()),
                ('user_type', models.IntegerField()),
            ],
            options={
                'db_table': 'school_user',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('contact', models.DecimalField(decimal_places=0, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='studentMgt.School_user')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Student_in_class',
            fields=[
                ('student_class_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('roll_no', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_in_class', to='studentMgt.Course_Class')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_in_class', to='studentMgt.Student')),
            ],
            options={
                'db_table': 'student_in_class',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=30)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='studentMgt.Course_Class')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('contact', models.DecimalField(decimal_places=0, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='studentMgt.School_user')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='studentMgt.Teacher'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='studentMgt.School_user'),
        ),
        migrations.AddField(
            model_name='marks',
            name='student_class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='studentMgt.Student_in_class'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='studentMgt.Subject'),
        ),
        migrations.AddField(
            model_name='course_class',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_class', to='studentMgt.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='studentMgt.Department'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='studentMgt.Course_Class'),
        ),
    ]
