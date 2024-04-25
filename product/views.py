from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Product , ProductImages , Brand , Review

class ProductList(ListView):
  model = Product

class ProductDetail(DeleteView):
  model = Product