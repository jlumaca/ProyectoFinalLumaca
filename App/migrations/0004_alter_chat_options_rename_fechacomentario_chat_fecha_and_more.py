# Generated by Django 5.0.6 on 2024-06-22 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_vehiculo_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['fecha']},
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='fechaComentario',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='nombre',
            new_name='nombreCompleto',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='chat',
            name='consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='App.vehiculo'),
        ),
        migrations.AddField(
            model_name='chat',
            name='telefono',
            field=models.CharField(default=None, max_length=20),
        ),
    ]