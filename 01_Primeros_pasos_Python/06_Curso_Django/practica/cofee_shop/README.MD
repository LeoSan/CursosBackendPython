# Es una practica básica para aprender y mejorar como se hace un proyecto en Django 

## Comandos utiles 
- para activar entorno -> ´source django_one/bin/activate´
- Para migrate -> ´python manage.py makemigrations´ -> ´python manage.py migrate´
- Para correr el server -> ´python3 manage.py runserver´
- Para entrar al shellDB -> ´python3 manage.py dbshell´
- Crear super usuario -> ´python3 manage.py createsuperuser´
- Comando para crear app ->  ´python3 manage.py startapp my_first_app´
- Debuguear -> {% debug order %} -> Es la forma de debuguer dentro de una plantilla la variable order es los que manejamos en el context_object_name de 
las viwe.py
- Instalar django-rest-framework -> ´pip3 install django-rest-framework´



## Notas Mentales 
- El python3 -> es porque mi ambiente instale la version 3 hay que validar eso ya que en los comandos debes hacer el ajuste de quitar python3 en caso que no se tenga instaldo 
- Si te topas con el error de las rutas recuerda que no hace match -> no es lo mismo http://127.0.0.1:8000/usuarios/login/ -> http://127.0.0.1:8000/usuarios/login -> solo le falta el slah (/) al final de la url 
- Admin.py cada APP generarada tiene este archivo admin aqui ppodremos gestionar para registrar esta app y pueda ser usada desde el modulo admin ya con su CRUD integrado [Ejemplo](../cofee_shop/products/admin.py)
- Recuerda si haces un ajuste asi sea minimos se debe ejecutar los comandos migartes 
- Podemos generar formulario ya usando los MODELOS 
    - Forma de generar formulario usando el modelo 
    ´´´python
    from django.forms import ModelForm # Podemos usar Los modelos para generar Formularios 
    from .models import OrderProduct


    class OrderProductForm(ModelForm):
        class Meta:
            model = OrderProduct
            fields = ["product"]

´´´

## Modelos 
- User
- Products
- Orden

## Librerias extras 


## crispy-tailwind==1.0.3
- https://github.com/django-crispy-forms/crispy-tailwind 
- Paso 1: pip install crispy-tailwind
- Paso 2: configuramos INSTALLED_APPS -> 
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_tailwind",
    ...
)

- Paso 3: para usar este pluging en los firmularios debemos llamarlos de la siguiente manera 
    - 1.  Load the filter: {% load tailwind_filters %}
    - 2. Apply the crispy filter: {{ form|crispy }} 
