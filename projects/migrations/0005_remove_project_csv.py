# Generated by Django 4.2.7 on 2023-11-15 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_csv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='csv',
        ),
    ]
