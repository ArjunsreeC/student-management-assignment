# Generated by Django 3.1.1 on 2020-10-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_remove_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]
