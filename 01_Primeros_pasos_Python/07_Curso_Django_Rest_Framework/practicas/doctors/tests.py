from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor


class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Luis',
            last_name='Martinez',
            date_of_birth='1990-12-05',
            contact_number='12312312',
            email='example@example.com',
            address='Dirección de prueba',
            medical_history='Ninguna',
        )
        self.doctor = Doctor.objects.create(
            first_name='Oscar',
            last_name='Barajas',
            qualification='Profesional',
            contact_number='23412341234',
            email='example2@example.com',
            address='Medellín',
            biography='Sin',
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments',
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)