# Generated by Django 4.1.2 on 2022-11-04 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_progress_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='complete',
            new_name='status',
        ),
    ]