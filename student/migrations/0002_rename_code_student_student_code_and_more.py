# Generated by Django 5.0.6 on 2024-07-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='code',
            new_name='student_code',
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_bio',
            field=models.TextField(null=True),
        ),
    ]