# Generated by Django 4.2.6 on 2023-11-03 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_instructor'),
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.course'),
        ),
    ]