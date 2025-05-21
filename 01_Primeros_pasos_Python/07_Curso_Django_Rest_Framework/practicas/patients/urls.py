
from django.urls import path
from patients.views import ListPatientsView, DetailPatientsView

urlpatterns = [
    path('paciente', ListPatientsView.as_view()),
    path('paciente/<int:pk>', DetailPatientsView.as_view()),
    #path('paciente',  list_patients),
    #path('/paciente/crear',  create_patient),
    #path('/paciente/detalle/<int:pk>',  detail_patients),
    #path('/paciente/editar/<int:pk>',  edit_patient),
    #path('/paciente/eliminar/<int:pk>',  delete_patient),
]
