# Generated by Django 5.0.3 on 2024-03-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipos', '0002_remove_tecnico_num_camisa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='num_camisa',
            field=models.IntegerField(blank=True, null=True, verbose_name='Num_Camisa'),
        ),
    ]