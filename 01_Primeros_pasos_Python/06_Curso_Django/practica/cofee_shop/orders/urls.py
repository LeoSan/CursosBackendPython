from django.urls import path
from django.http import HttpResponse
from .views import MyOrderView, CreateOrderProductView

def test_view(request:any):
    print('entre -------Ordenes------')
    return HttpResponse("¡La vista de prueba en la app 'usuarios' funciona correctamente!")

urlpatterns = [
    path('test/', test_view, name="test"),  # URL de prueba
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateOrderProductView.as_view(), name="add_product"),
]