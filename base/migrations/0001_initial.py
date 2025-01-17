# Generated by Django 4.2.9 on 2024-04-16 18:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_num', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_addr', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
