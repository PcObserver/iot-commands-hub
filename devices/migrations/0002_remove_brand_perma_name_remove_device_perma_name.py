# Generated by Django 5.0.4 on 2024-04-30 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='perma_name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='perma_name',
        ),
    ]