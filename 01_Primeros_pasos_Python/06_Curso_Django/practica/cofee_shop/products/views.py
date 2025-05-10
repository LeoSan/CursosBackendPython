import genericpath
#from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

class ProductsFormView(genericpath.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm 

