# Generated by Django 4.1.4 on 2022-12-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_pessoa_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='cargo',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ManyToManyField(to='autenticacao.cargos'),
        ),
    ]
