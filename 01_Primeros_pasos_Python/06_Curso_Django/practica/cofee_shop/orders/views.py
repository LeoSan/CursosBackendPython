from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)  ## Permite generaar unn error controlado
from django.urls import reverse_lazy

from .models import Order
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = (
        "order"  ## Esto es importante porque si no no lo podemos ver en el html
    )

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, created = (
            Order.objects.get_or_create(  ## Es como el CreateOrUpdate de laravel del ORM
                is_active=True,
                user=self.request.user,
            )
        )  ## Devuelve dos valores el objeto creado y un valor true o false para validar
        # if created == True:
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
