# Generated by Django 4.0.4 on 2022-05-29 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0019_remove_propostas_usuario_propostas_pedido_fk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propostas',
            name='usuarioPedido_fk',
        ),
    ]
