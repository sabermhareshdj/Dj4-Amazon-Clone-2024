from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView
from .models import Product , ProductImages , Brand , Review
from django.db.models import Q , F , Value
from django.db.models.aggregates import Max,Min,Count,Avg,Sum
from django.views.decorators.cache import cache_page
from .tasks import send_emails

from django.http import JsonResponse   #اجاكس
from django.template.loader import render_to_string #اجاكس 


# @cache_page(60 * 1)
def queryset_dubug(request):
  #data = Product.objects.select_related('brand').all() # select_related with ForeignKey and one_to_one
                                                       # prefetch_related  with many_to_many
  # filter 
  #data = Product.objects.filter(price__gt = 70) اكبر من
  #data = Product.objects.filter(price__gte = 70) اكبر من او يساوي
  #data = Product.objects.filter(price__lt = 70) اقل من
  #data = Product.objects.filter(price__lte = 70) اقل من او يساوي
  #data = Product.objects.filter(price__range = (65 , 70)) الاسعار بين
  # navigate relation 
  #data = Product.objects.filter(brand__name="Apple")
  #data = Product.objects.filter(brand__price__gt = 70)
  # filter with text 
  #data = Product.objects.filter(name__contains = 'rown')
  #data = Product.objects.filter(name__startswith='Jacob')
  #data = Product.objects.filter(name__endswith='e')
  #data = Product.objects.filter(tags__isnull=True)
  #filter date time 
  #data = Review.objects.filter(created_at__year=2023)
  #data = Review.objects.filter(created_at__month=  )
  #filter 2 values
  #data = Product.objects.filter(price__gt=80 , quantity__lt =10 )

  # data = Product.objects.filter(
  #   Q(price__gt=80) |
  #   Q(quantity__lt =10) )

  # data = Product.objects.filter(
  # Q(price__gt=80) &
  # Q(quantity__lt =10) )

  # data = Product.objects.filter(
  # Q(price__gt=80) &
  # ~Q(quantity__lt =10) ) # عكس المطلوب اي اقل 
  # field lookup
  #data = Product.objects.filter(price = F('quantity') ) # F field ,  مقارنة عمود في عمود 
  #########################
  #data = Product.objects.all().order_by('name') # شبيه بالسطر التحته
  #data = Product.objects.order_by('name') #ASC تصاعدي
  #data = Product.objects.order_by('-name') #DES تنازلي (-)
  #data = Product.objects.order_by('name','quantity')
  #data = Product.objects.order_by('name','-quantity')
  #data = Product.objects.order_by('name')[0]  #first
  #data = Product.objects.order_by('name')[-1] # last
  #data = Product.objects.earliest('name')  #first
  #data = Product.objects..latest('name') # last
  #data = Product.objects.all()[:10]
  #data = Product.objects.all()[10:20]

  # select columns
  #data = Product.objects.values('name','price')
  #data = Product.objects.values('name','price','brand__name')
  #data = Product.objects.values_list('name','price','brand__name')

  #remove duplicate
  #data = Product.objects.all().distinct()
  
  #data = Product.objects.only('name','price')
  #data = Product.objects.defer('slug')  # ما عدا 
  #data = Product.objects.defer('slug','description')

  #aggregation  عمليات حسابية (تجميعية)
  #data = Product.objects.aaggregate(Sum('quantity'))
  #data = Product.objects.aaggregate(Avg('price'))
  # annotate اضافة عمود بناء على عملية حسابية 

  # data = Product.objects.annotate(price_with_tax=F('price') * 1.2)

  data = Product.objects.get(id=1993)

  send_emails.delay()


  return render(request,'product/debug.html',{'data':data})


class ProductList(ListView):
  model = Product
  paginate_by = 30            # context : object_list , model_list 

class ProductDetail(DetailView):
  model = Product             # context : object , model

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["reviews"] = Review.objects.filter(product=self.get_object())
    context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
    return context


class BrandList(ListView):
  model = Brand             # context : object_list , brand_list
  queryset = Brand.objects.annotate(product_count=Count('product_brand'))
  paginate_by = 20 

  

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
    context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
    return context
  

def add_review(request,slug):


  product = Product.objects.get(slug=slug)


  rate = request.POST['rate']    
  review = request.POST['review']

  Review.objects.create(
    product = product ,
    rate= rate ,
    review = review ,
    user = request.user
    )
  # reviews  اجاكس
  reviews = Review.objects.filter(product=product)
  html = render_to_string('include/reviews_include.html',{'reviews ':reviews })
  return JsonResponse({'result':html})
#return redirect(f'/products/{product.slug}')