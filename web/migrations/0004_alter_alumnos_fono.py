# Generated by Django 4.1 on 2022-11-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_ciudad_matricula_sucursal_remove_matriculas_alumrut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='fono',
            field=models.CharField(max_length=10),
        ),
    ]
