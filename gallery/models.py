from django.db import models
import os
# Create your models here.

class MyariSaponi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/MyariSaponi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = MyariSaponi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except MyariSaponi.DoesNotExist:
            pass

    super(MyariSaponi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(MyariSaponi, self).delete(*args, **kwargs)

class Tsubi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/Tsubi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Tsubi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Tsubi.DoesNotExist:
            pass

    super(Tsubi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Tsubi, self).delete(*args, **kwargs)

class PetBotli(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/PetBotli', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = PetBotli.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except PetBotli.DoesNotExist:
            pass

    super(PetBotli, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(PetBotli, self).delete(*args, **kwargs)

class Chusti(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/Chusti', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Chusti.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Chusti.DoesNotExist:
            pass

    super(Chusti, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Chusti, self).delete(*args, **kwargs)

class Dispenserebi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True,)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/Dispenserebi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Dispenserebi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Dispenserebi.DoesNotExist:
            pass

    super(Dispenserebi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Dispenserebi, self).delete(*args, **kwargs)


class EliteAlternative(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='static/img/EliteAlternative', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = EliteAlternative.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except EliteAlternative.DoesNotExist:
            pass

    super(EliteAlternative, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(EliteAlternative, self).delete(*args, **kwargs)
