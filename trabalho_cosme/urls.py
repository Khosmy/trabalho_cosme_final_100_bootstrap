from django.conf.urls import patterns, include, url
from django.contrib import admin
from cadastro.views import*

urlpatterns = patterns('',   
	#essentials utls
	url(r'^$', 'classes.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	#cadurls
	url(r'^cadCli/', 'classes.views.cadCli', name="cadCli"),
	url(r'^cadVaga/', 'classes.views.cadVaga', name="cadVaga"),
	url(r'^cadCar/', 'classes.views.cadCar', name="cadCar"),
	url(r'^cadAlug/', 'classes.views.cadAlug', name="cadAlug"),	
	#visualizar
	url(r'^cliente/', 'classes.views.cliente', name="cliente"),
	url(r'^vaga/', 'classes.views.vaga', name="vaga"),
	url(r'^carro/', 'classes.views.carro', name="carro"),
	url(r'^alugar/', 'classes.views.alugar', name="alugar"),		
	# editar 
	url(r'^eCliente/(.*)', 'classes.views.eCliente', name="eCliente"),
	url(r'^eCarro/(.*)', 'classes.views.eCarro', name="eCarro"),
	url(r'^eVaga/(.*)', 'classes.views.eVaga', name="eVaga"),
	url(r'^eAlugar/(.*)', 'classes.views.eAlugar', name="eAlugar"),
	
)
