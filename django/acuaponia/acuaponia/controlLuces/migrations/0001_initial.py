# Generated by Django 4.0.4 on 2022-05-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programacion_luces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_encendido', models.IntegerField(blank=b'I01\n')),
                ('minuto_encendido', models.IntegerField(blank=b'I01\n')),
                ('hora_apagado', models.IntegerField(blank=b'I01\n')),
                ('minuto_apagado', models.IntegerField(blank=b'I01\n')),
            ],
            options={
                'verbose_name_plural': 'Programacion de luces',
            },
        ),
    ]
