
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls')),
    path('orders/', include('orders.urls',namespace='orders')),
    path('', include('settings.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path('rosetta/', include('rosetta.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)