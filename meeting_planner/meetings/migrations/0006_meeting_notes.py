# Generated by Django 3.2 on 2023-05-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_auto_20230517_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='notes',
            field=models.TextField(default='none'),
        ),
    ]