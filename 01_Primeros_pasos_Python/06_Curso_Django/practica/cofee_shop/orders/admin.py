# Register your models here.
from django.contrib import admin
from .models import Order, OrderProduct

"""

admin.TabularInline: Esto indica que la clase OrderProductInlineAdmin hereda de la clase TabularInline que se encuentra 
dentro del módulo admin. 

TabularInline es una clase de Django que permite mostrar modelos relacionados (en este caso, OrderProduct) 
directamente dentro de la página de edición de otro modelo (en este caso, Order), presentándolos en un formato de tabla.
"""


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


"""
inlines = [OrderProductInlineAdmin]: Este atributo dentro de OrderAdmin es una 
lista que contiene otras clases InlineAdmin. 

En este caso, incluye OrderProductInlineAdmin. Esto es lo que permite que los objetos 
relacionados del modelo OrderProduct se muestren y se puedan editar directamente dentro 
de la página de administración del modelo Order
"""


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInlineAdmin
    ]  ## Esto permite hacer el macth con los productos


admin.site.register(Order, OrderAdmin)
