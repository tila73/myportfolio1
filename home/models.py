from django.db import models

# Create your models here.
class BioData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    education1 = models.CharField(max_length=100)
    education2 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name 

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()   

    def __str__(self):
        return self.name 

class Work(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title 

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=350)

    def __str__(self):
        return self.full_name