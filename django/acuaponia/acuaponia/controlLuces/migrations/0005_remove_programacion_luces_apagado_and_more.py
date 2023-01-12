# Generated by Django 4.0.4 on 2022-05-27 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlLuces', '0004_alter_programacion_luces_apagado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacion_luces',
            name='apagado',
        ),
        migrations.RemoveField(
            model_name='programacion_luces',
            name='encendido',
        ),
        migrations.AddField(
            model_name='programacion_luces',
            name='hora_apagado',
            field=models.PositiveSmallIntegerField(blank=b'I01\n', choices=[(datetime.time(0, 0), '00:00'), (datetime.time(1, 0), '01:00'), (datetime.time(2, 0), '02:00'), (datetime.time(3, 0), '03:00'), (datetime.time(4, 0), '04:00'), (datetime.time(5, 0), '05:00'), (datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00'), (datetime.time(23, 0), '23:00')], null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='programacion_luces',
            name='hora_encendido',
            field=models.PositiveSmallIntegerField(blank=b'I01\n', choices=[(datetime.time(0, 0), '00:00'), (datetime.time(1, 0), '01:00'), (datetime.time(2, 0), '02:00'), (datetime.time(3, 0), '03:00'), (datetime.time(4, 0), '04:00'), (datetime.time(5, 0), '05:00'), (datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00'), (datetime.time(23, 0), '23:00')], null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='programacion_luces',
            name='minuto_apagado',
            field=models.PositiveSmallIntegerField(blank=b'I01\n', null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='programacion_luces',
            name='minuto_encendido',
            field=models.PositiveSmallIntegerField(blank=True, null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
    ]
