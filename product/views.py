from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Review

class ProductList(ListView):
  model = Product             # context : object_list , model_list 

class ProductDetail(DetailView):
  model = Product             # context : object , model

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["reviews"] = Review.objects.filter(product=self.get_object())
    context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
    return context


class BrandList(ListView):
  model = Brand             # context : object_list , brand_list



class BrandDetail(ListView):
  model = Product
  template_name = 'product/brand_detail.html'
  paginate_by = 20 

  def get_queryset(self): # overide quary
    brand = Brand.objects.get(slug=self.kwargs['slug'])
    return super().get_queryset().filter(brand=brand)
  
  # retrieve new data : template 
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
    return context