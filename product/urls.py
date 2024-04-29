from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , queryset_dubug
from .api import product_list_api , product_detail_api , ProductDetailAPI , ProductListAPI


urlpatterns = [
    path('', ProductList.as_view()),
    path('debug', queryset_dubug),

    path('<slug:slug>', ProductDetail.as_view()),

    path('brands/' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),

    # api
    path('api/list' , ProductListAPI.as_view()),
    path('api/list/<int:pk>' , ProductDetailAPI.as_view()),
]
