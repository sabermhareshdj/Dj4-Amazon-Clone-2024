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
