from django.shortcuts import render
from django.http import HttpResponse
from .models import MyariSaponi, Tsubi, PetBotli, Chusti, Dispenserebi, EliteAlternative


def index(req):
  products = MyariSaponi.objects.all()
  return render(req, 'index.html', {'products': products})

def tsubi(req):
  products = Tsubi.objects.all()
  return render(req, 'index.html', {'products': products})


def petBotli(req):
  products = PetBotli.objects.all()
  return render(req, 'index.html', {'products': products})

def chusti(req):
  products = Chusti.objects.all()
  return render(req, 'index.html', {'products': products})

def dispenserebi(req):
  products = Dispenserebi.objects.all()
  return render(req, 'index.html', {'products': products})

def eliteAlternative(req):
  products = EliteAlternative.objects.all()
  return render(req, 'index.html', {'products': products})