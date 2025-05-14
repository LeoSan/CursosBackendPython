from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=200, verbose_name="nombre")

    def __str__(self):
        return f"{self.name} "