from django.urls import path
from .views import ProductsFormView, ProductsListView, ProductListAPI

urlpatterns = [
    path("listado/", ProductsListView.as_view(), name="list_product"),
    path("agregar/", ProductsFormView.as_view(), name="add_product"),
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
]
