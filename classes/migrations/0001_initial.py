# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tempo', models.DateTimeField(null=True, verbose_name=b'Data e Hora')),
                ('Valor', models.DecimalField(null=True, verbose_name=b'Valor', max_digits=20, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Modelo', models.CharField(max_length=100, null=True, verbose_name=b'Modelo')),
                ('Marca', models.CharField(max_length=100, null=True, verbose_name=b'Marca')),
                ('Placa', models.CharField(max_length=10, null=True, verbose_name=b'Placa')),
                ('Cor', models.CharField(max_length=20, null=True, verbose_name=b'Cor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endere\xc3\xa7o')),
                ('Numero', models.IntegerField(max_length=10, null=True, verbose_name=b'N\xc3\xbamero')),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cpf', models.CharField(max_length=11, null=True, verbose_name=b'CPF')),
                ('Contato', models.CharField(max_length=15, null=True, verbose_name=b'Contato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Numero', models.CharField(max_length=10, verbose_name=b'Vaga')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alugar',
            name='Carro',
            field=models.ForeignKey(to='classes.Carro', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alugar',
            name='Cliente',
            field=models.ForeignKey(to='classes.Cliente', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alugar',
            name='Vaga',
            field=models.ForeignKey(to='classes.Vaga', null=True),
            preserve_default=True,
        ),
    ]
