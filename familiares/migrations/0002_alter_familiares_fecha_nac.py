# Generated by Django 4.0.4 on 2022-05-25 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='fecha_nac',
            field=models.DateField(),
        ),
    ]