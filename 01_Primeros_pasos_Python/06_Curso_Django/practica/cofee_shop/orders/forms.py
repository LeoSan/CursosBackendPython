from django.forms import ModelForm # Podemos usar Los modelos para generar Formularios 
from .models import OrderProduct


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]