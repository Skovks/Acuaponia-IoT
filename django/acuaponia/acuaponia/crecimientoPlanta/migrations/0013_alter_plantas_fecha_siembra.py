# Generated by Django 4.0.4 on 2022-05-10 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crecimientoPlanta', '0012_alter_plantas_fecha_siembra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantas',
            name='fecha_siembra',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
