# Generated by Django 4.1.2 on 2023-03-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0003_alter_prestador_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestador',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]