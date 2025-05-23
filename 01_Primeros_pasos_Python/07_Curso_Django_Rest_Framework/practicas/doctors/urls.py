from django.urls import path

from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)## Permite regitsrar un viewset

urlpatterns = [
    ##path('doctors/', ListDoctorView.as_view()), ##Antes   
    ##path('doctors/<int:id>/', DetailDoctorView.as_view()), ## Antes 
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:id>/', DetailDepartmentView.as_view()),
    path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
    path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
] + router.urls ## Ahora Esta linea permite anclar las url nuevas de doctor ya que fueron registradas 