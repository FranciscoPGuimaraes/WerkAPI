# Generated by Django 4.2.4 on 2023-09-17 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demandas', '0010_demanda_update_alter_demanda_preco_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demanda',
            old_name='prestadroCPF',
            new_name='prestadorCPF',
        ),
    ]
