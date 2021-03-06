# Generated by Django 4.0.1 on 2022-01-30 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equip_slot', models.CharField(choices=[('IN', 'Inventory'), ('HE', 'Head'), ('CH', 'Chest'), ('LE', 'Legs'), ('FE', 'Feet'), ('RL', 'Ring Left'), ('RR', 'Ring Right')], default='IN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last_modified')),
                ('current_server_key', models.BinaryField(blank=True, max_length=50)),
                ('current_server_key_salt', models.BinaryField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Savestate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_level', models.CharField(choices=[('DE', 'Default'), ('D1', 'Dungeon 1')], default='DE', max_length=2)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(through='server.EquipSlot', to='server.Item')),
            ],
        ),
        migrations.AddField(
            model_name='equipslot',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.inventory'),
        ),
        migrations.AddField(
            model_name='equipslot',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.item'),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last_modified')),
                ('hp_max', models.PositiveIntegerField()),
                ('hp_current', models.PositiveIntegerField()),
                ('level', models.PositiveIntegerField(default=1)),
                ('class_type', models.CharField(choices=[('DEFAULT', 'Default'), ('WARRIOR', 'Warrior'), ('RANGER', 'Ranger'), ('WIZARD', 'Wizard')], default='DEFAULT', max_length=20)),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='server.inventory')),
                ('savestate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='server.savestate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
