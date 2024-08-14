from django.db import models
import os
# Create your models here.

class Amenitebi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='Amenitebi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Amenitebi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Amenitebi.DoesNotExist:
            pass

    super(Amenitebi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Amenitebi, self).delete(*args, **kwargs)

class TavisMovla(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='TavisMovla', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = TavisMovla.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except TavisMovla.DoesNotExist:
            pass

    super(TavisMovla, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(TavisMovla, self).delete(*args, **kwargs)

class Saponi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='Saponi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Saponi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Saponi.DoesNotExist:
            pass

    super(Saponi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Saponi, self).delete(*args, **kwargs)

class Chusti(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='Chusti', blank=True)
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
  photo = models.ImageField(upload_to='Dispenserebi', blank=True)
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


class Partniorebi(models.Model):
  header = models.CharField(max_length=255)
  headerEng = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='Partniorebi', blank=True)
  def save(self, *args, **kwargs):
    # Check if the instance already exists in the database
    if self.pk:
        try:
            old_instance = Partniorebi.objects.get(pk=self.pk)
            if old_instance.photo and self.photo and old_instance.photo != self.photo:
                # Delete the old photo if a new photo is being uploaded
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        except Partniorebi.DoesNotExist:
            pass

    super(Partniorebi, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      if self.photo:
          if os.path.isfile(self.photo.path):
              os.remove(self.photo.path)
      super(Partniorebi, self).delete(*args, **kwargs)