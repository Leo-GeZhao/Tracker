# Generated by Django 4.1.2 on 2022-11-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_progress_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
