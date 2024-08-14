from django.shortcuts import render
from django.http import HttpResponse
from .models import Amenitebi, TavisMovla, Saponi, Chusti, Dispenserebi, Partniorebi


def index(req):
  products = Amenitebi.objects.all()
  return render(req, 'index.html', {'products': products})

def tavisMovla(req):
  products = TavisMovla.objects.all()
  return render(req, 'index.html', {'products': products})


def saponi(req):
  products = Saponi.objects.all()
  return render(req, 'index.html', {'products': products})

def chusti(req):
  products = Chusti.objects.all()
  return render(req, 'index.html', {'products': products})

def dispenserebi(req):
  products = Dispenserebi.objects.all()
  return render(req, 'index.html', {'products': products})

def partniorebi(req):
  products = Partniorebi.objects.all()
  return render(req, 'index.html', {'products': products})