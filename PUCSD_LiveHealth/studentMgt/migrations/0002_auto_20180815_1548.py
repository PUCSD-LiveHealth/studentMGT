# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentMgt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_name',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course_class',
            name='class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='school_user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_in_class',
            name='student_class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
