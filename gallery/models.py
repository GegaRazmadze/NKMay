from django.db import models

# Create your models here.

class MyariSaponi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/MyariSaponi', blank=True)

class Tsubi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/Tsubi', blank=True)

class PetBotli(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/PetBotli', blank=True)

class Chusti(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/Chusti', blank=True)

class Dispenserebi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True,)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/Dispenserebi', blank=True)


class EliteAlternative(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.FloatField()
  photo = models.ImageField(upload_to='gallery/static/img/EliteAlternative', blank=True)
