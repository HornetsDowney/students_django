# Generated by Django 3.1.2 on 2020-10-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201013_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_password',
            field=models.IntegerField(),
        ),
    ]
