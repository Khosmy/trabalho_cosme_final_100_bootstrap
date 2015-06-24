from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from models import *
from forms import *

def index(request):		
	return render(request,'index.html')	

# cadastrar editar	
#CLIENTE
def cliente(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Cliente.objects.filter(Nome__contains=pesquisar)
	else:
		post = Cliente.objects.all()
	return render(request,'cliente.html',{'post': post})		
	
def eCliente(request,id=None):
	obj = get_object_or_404(Cliente, pk=id)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('cliente')
	else:	
		form = ClienteForm(instance=obj) 
	return render(request,"cadCli.html",{'form':form})
		
def cadCli(request):	
	if request.method == 'POST':	
		form = ClienteForm(request.POST) 
		form.save()
		return redirect('cadCli')
	else:
		form = ClienteForm() 
		return render(request,"cadCli.html",{'form':form})				
#CARRO
def carro(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Carro.objects.filter(Modelo__contains=pesquisar)
	else:
		post = Carro.objects.all()
	return render(request,'carro.html',{'post': post})

def eCarro(request,id=None):
	obj = get_object_or_404(Carro, pk=id)
	if request.method == 'POST':
		form = CarroForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('carro')
	else:	
		form = CarroForm(instance=obj) 
	return render(request,"cadCar.html",{'form':form})
	
def cadCar(request):		
	if request.method == 'POST':
		form = CarroForm(request.POST) 
		form.save()
		return redirect('cadCar')
	else:
		form = CarroForm() 
		return render(request,"cadCar.html",{'form':form})
#VAGA
def vaga(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Vaga.objects.filter(Numero__contains=pesquisar)
	else:
		post = Vaga.objects.all()
	return render(request,'vaga.html',{'post': post})

def eVaga(request,id=None):
	obj = get_object_or_404(Vaga, pk=id)
	if request.method == 'POST':
		form = VagaForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('vaga')
	else:	
		form = VagaForm(instance=obj) 
	return render(request,"cadVaga.html",{'form':form})
	
def cadVaga(request):		
	if request.method == 'POST':
		form = VagaForm(request.POST) 
		form.save()
		return redirect('cadVaga')
	else:
		form = VagaForm() 
		return render(request,"cadVaga.html",{'form':form})	
#ALUGAR
def alugar(request):
	if request.method == 'POST':
		pesquisar = request.POST.get('pesquisar')
		post = Alugar.objects.filter(Cliente__contains=pesquisar)
	else:
		post = Alugar.objects.all()
	return render(request,'alugar.html',{'post': post})
	
def eAlugar(request,id=None):
	obj = get_object_or_404(Alugar, pk=id)
	if request.method == 'POST':
		form = AlugarForm(request.POST, instance=obj) 
		if form.is_valid():
			form.save()
			return redirect('alugar')
	else:	
		form = AlugarForm(instance=obj) 
	return render(request,"cadAlug.html",{'form':form})	
	
def cadAlug(request):		
	if request.method == 'POST':
		form = AlugarForm(request.POST) 
		form.save()
		return redirect('cadAlug')
	else:
		form = AlugarForm() 
		return render(request,"cadAlug.html",{'form':form})		
		