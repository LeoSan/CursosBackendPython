from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year  = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=10, null=True)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.color} "
    
class Publisher(models.Model):
    name = models.TextField(max_length=250, null=True, default='n/a')
    direccion = models.TextField(max_length=250, null=True, default='n/a')

    def __str__(self):
        return f"{self.name} - {self.direccion} "
    
class Autor(models.Model):
    nombre = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.nombre
    
class Profile(models.Model):
    website = models.URLField(max_length=200)
    biography = models.TextField(max_length=500)
    author = models.OneToOneField(Autor, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField(Autor, related_name="authors", null=True) ## Muy importante el orden por eso el Autor esta en la parte superior

    def __str__(self):
        return self.title


