# Generated by Django 4.0.1 on 2022-01-30 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='inventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='character',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='server.character'),
            preserve_default=False,
        ),
    ]