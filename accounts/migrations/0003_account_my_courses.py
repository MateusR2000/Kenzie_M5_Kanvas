# Generated by Django 4.2.6 on 2023-11-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0001_initial'),
        ('courses', '0005_alter_course_instructor'),
        ('accounts', '0002_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='my_courses',
            field=models.ManyToManyField(related_name='my_courses', through='students_courses.StudentCourse', to='courses.course'),
        ),
    ]