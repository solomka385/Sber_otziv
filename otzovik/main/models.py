from django.db import models



class Personal(models.Model):
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    job = models.CharField(max_length=50)
    date_of_dirth = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Transport(models.Model):
    user = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    image = models.ImageField()

class Anketa(models.Model):
    user = models.CharField(max_length=50, unique=True)
    number1 = models.CharField(max_length=50, blank=True)
    number2 = models.CharField(max_length=50,blank=True)
    number3 = models.CharField(max_length=50,blank=True)
    number4 = models.CharField(max_length=50,blank=True)
    number5 = models.CharField(max_length=50,blank=True)

class Opros(models.Model):
    user = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)