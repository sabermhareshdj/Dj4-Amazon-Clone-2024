from django.contrib import admin

from .models import Profile , Phone , Address

admin.site.register(Profile)
admin.site.register(Phone)
admin.site.register(Address)