from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Products

# Create your views here.

class ProductsFormView(generic.FormView):
    template_name = "product/add_product.html"
    form_class = ProductForm 
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_invalid(form)
    

class ProductsListView(generic.ListView):
    model = Products
    template_name = "product/list_product.html"
    context_object_name = 'products'