# Generated by Django 4.0.1 on 2022-01-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_profile_current_server_key_salt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_server_key',
            field=models.BinaryField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_server_key_salt',
            field=models.BinaryField(blank=True, max_length=50),
        ),
    ]