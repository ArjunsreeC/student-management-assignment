# Generated by Django 3.1.1 on 2020-10-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_auto_20201008_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='regno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
