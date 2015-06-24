#-*- encoding: utf-8 -*-
from django import forms
from models import Cliente
from models import Carro
from models import Vaga
from models import Alugar
 
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome','Endereco','Numero','Bairro','Cpf','Contato']

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['Modelo','Marca','Placa','Cor']	

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['Numero']			
		
class AlugarForm(forms.ModelForm):
    class Meta:
        model = Alugar
        fields = ['Vaga','Carro','Cliente','Tempo','Valor']				