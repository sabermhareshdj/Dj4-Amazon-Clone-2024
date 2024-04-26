from django.shortcuts import render
from django.views.generic import ListView , DeleteView
from .models import Product , ProductImages , Brand , Review

class ProductList(ListView):
  model = Product             # context : object_list , model_list 

class ProductDetail(DeleteView):
  model = Product             # context : object , model