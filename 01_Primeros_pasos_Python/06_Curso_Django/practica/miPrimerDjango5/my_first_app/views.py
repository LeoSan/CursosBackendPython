from django.shortcuts import render
from .models import Autor, Profile, Book

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"},
        {"title": "Toyota"},
        {"title": "Honda"},
        {"title": "Ford"},
        {"title": "Mercedes-Benz"},
        {"title": "Audi"},
        {"title": "Volkswagen"},
        {"title": "Nissan"},
        {"title": "Chevrolet"}
    ]
    context = {"car_list": car_list}
    return render(request, 'my_first_app/car_list.html', context)

def view_autores(request, *args, **kwargs):
    author = Autor.objects.get(id=kwargs['id'])
    context = {"autor": author}
    return render(request, 'my_first_app/autor_list.html', context)

def view_books(request):
    books = Book.objects.all() 
    context = {"book_list": books}
    return render(request, 'my_first_app/book_list.html', context)

