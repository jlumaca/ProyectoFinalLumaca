# Generated by Django 5.0.6 on 2024-06-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_vehiculo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
