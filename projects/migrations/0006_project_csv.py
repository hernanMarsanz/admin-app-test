# Generated by Django 4.2.7 on 2023-11-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='csv',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]