# Generated by Django 5.0.4 on 2024-04-24 00:15

import django.db.models.deletion
import json.decoder
import json.encoder
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contributions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('contribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contributions.contribution')),
                ('display_name', models.CharField(max_length=100, unique=True)),
                ('perma_name', models.CharField(max_length=100, unique=True)),
                ('prefix', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
            bases=('contributions.contribution',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('contribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contributions.contribution')),
                ('display_name', models.CharField(max_length=100, unique=True)),
                ('perma_name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='devices.brand')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
            bases=('contributions.contribution',),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('contribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contributions.contribution')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('payload', models.JSONField(decoder=json.decoder.JSONDecoder, encoder=json.encoder.JSONEncoder)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='actions', to='devices.device')),
            ],
            options={
                'verbose_name': 'Action',
                'verbose_name_plural': 'Actions',
            },
            bases=('contributions.contribution',),
        ),
    ]
