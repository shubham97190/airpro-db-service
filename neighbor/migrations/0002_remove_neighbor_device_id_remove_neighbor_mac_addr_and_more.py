# Generated by Django 4.2.9 on 2024-04-16 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbor',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='neighbor',
            name='mac_addr',
        ),
        migrations.RemoveField(
            model_name='neighbor',
            name='serial_num',
        ),
        migrations.AddField(
            model_name='neighbor',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.devicemodel'),
            preserve_default=False,
        ),
    ]
