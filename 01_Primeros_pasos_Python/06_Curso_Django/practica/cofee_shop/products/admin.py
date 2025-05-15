from django.contrib import admin
from .models import Products


# Register your models here.
# Paso 1: genero la clase que podra administrar el modelo esto se hace para genrar un CRUD
class ProductAdmin(admin.ModelAdmin):
    model = Products
    list_display = ["name", "price"]
    search_fields = ["name"]


# Paso 2: registramos y relacionamos modelo, con la clase que se genero aqui para el admin del modelo
admin.site.register(Products, ProductAdmin)
