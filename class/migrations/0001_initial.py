# Generated by Django 5.0.6 on 2024-06-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('sufficient_space', models.CharField(max_length=20)),
                ('learning_models', models.PositiveSmallIntegerField()),
                ('educational_resources', models.CharField(max_length=20)),
                ('chairs', models.PositiveSmallIntegerField()),
                ('tables', models.PositiveSmallIntegerField()),
                ('board', models.CharField(max_length=10)),
                ('students', models.PositiveSmallIntegerField(max_length=50)),
                ('windows', models.PositiveSmallIntegerField()),
                ('trainers', models.PositiveSmallIntegerField(max_length=20)),
            ],
        ),
    ]
