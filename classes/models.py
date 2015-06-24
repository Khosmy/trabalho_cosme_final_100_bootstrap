#-*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Cliente (models.Model):
	Nome = models.CharField('Nome',max_length=100, null=True)
	Endereco = models.CharField('Endereço',max_length=100, null=True)
	Numero = models.IntegerField('Número',max_length=10, null=True)
	Bairro = models.CharField('Bairro',max_length=100, null=True)
	Cpf = models.CharField('CPF',max_length=11, null=True)
	Contato = models.CharField('Contato',max_length=15, null=True)
	def __unicode__ (self):
		return self.Nome

class Carro (models.Model):
	Modelo = models.CharField('Modelo',max_length=100, null=True)
	Marca = models.CharField('Marca',max_length=100, null=True)
	Placa = models.CharField('Placa',max_length=10, null=True)
	Cor = models.CharField('Cor',max_length=20, null=True)
	def __unicode__ (self):
		return "%s - %s "%(self.Modelo,self.Placa)

class Vaga (models.Model):
	Numero = models.CharField('Vaga',max_length=10)
	def __unicode__(self):
		return "%s" % self.Numero

class Alugar (models.Model):
	Vaga = models.ForeignKey(Vaga,null=True)
	Carro = models.ForeignKey(Carro,null=True)
	Cliente = models.ForeignKey(Cliente,null=True)
	Tempo = models.DateTimeField('Data e Hora',null=True)
	Valor = models.DecimalField('Valor',max_digits=20,decimal_places=2,null=True)
	def __unicode__(self):
		return "%s - %s "%(self.Cliente,self.Carro)
