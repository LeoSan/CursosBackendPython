from django.urls import reverse_lazy
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .models import Products
from .serializers import ProductSerializer

# Create your views here.


class ProductsFormView(generic.FormView):
    template_name = "product/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_invalid(form)


class ProductsListView(generic.ListView):
    model = Products
    template_name = "product/list_product.html"
    context_object_name = "products"


class ProductListAPI(APIView):  ## Generar un API
    authentication_classes = []  ## Generar Permiso
    permission_classes = []  ## Generar permisos

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
