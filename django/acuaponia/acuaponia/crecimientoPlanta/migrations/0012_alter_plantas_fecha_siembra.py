# Generated by Django 4.0.4 on 2022-05-10 08:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crecimientoPlanta', '0011_alter_plantas_fecha_siembra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantas',
            name='fecha_siembra',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 8, 7, 39, 120005, tzinfo=utc)),
        ),
    ]
