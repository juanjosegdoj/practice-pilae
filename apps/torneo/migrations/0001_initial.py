# Generated by Django 2.0.3 on 2018-04-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('nombre', models.CharField(default='', max_length=70, primary_key=True, serialize=False, unique=True)),
                ('deporte', models.CharField(blank=True, choices=[('Baloncesto', 'Baloncesto'), ('Voleibol', 'Voleibol'), ('Micro-Futbol', 'Micro-Futbol')], default='Baloncesto', max_length=25, null=True)),
                ('fecha', models.DateField()),
                ('sexo', models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino'), ('MIX', 'Mixto')], max_length=3, null=True)),
            ],
        ),
    ]
