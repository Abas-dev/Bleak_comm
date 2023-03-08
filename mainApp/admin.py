from django.contrib import admin

from .models import Catergory, Products,Cart

admin.site.register(Catergory)
admin.site.register(Products)
admin.site.register(Cart)