from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.http import HttpResponse
from .views import RegisterView

def test_view(request:any):
    print('entre -------------')
    return HttpResponse("¡La vista de prueba en la app 'usuarios' funciona correctamente!")

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('test/', test_view, name="test"),  # URL de prueba
    path("registro/", RegisterView.as_view(), name="register"), 
]