from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'principais/index.html')

def noticias(request):
	return render(request,'principais/noticias.html')
	
def analise_sistemas(request):
	return render(request,'cursos/curso_analise_des_sistemas.html')

# Create your views here.
