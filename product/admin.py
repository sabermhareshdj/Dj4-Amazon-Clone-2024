from django.contrib import admin

from .models import Product , ProductImages , Brand , Review

class ProductImageTabular(admin.TabularInline):
  model = ProductImages

class ProductAdmin(admin.ModelAdmin):
  list_display = ['name','flag','price','quantity','brand']
  list_filter = ['flag','brand']
  search_fields = ['name','subtitle','description']
  inlines =[ProductImageTabular]




admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)