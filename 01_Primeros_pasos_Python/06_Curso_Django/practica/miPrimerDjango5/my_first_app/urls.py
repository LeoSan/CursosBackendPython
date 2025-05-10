from django.http import HttpResponse
from django.urls import path
from my_first_app.views import view_autores, view_books

def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

urlpatterns = [
    path('listado/', view_books),
    path('autor/<int:id>', view_autores),
]


