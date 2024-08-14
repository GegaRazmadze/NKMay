

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name="index"),
  path("tavisMovla", views.tavisMovla, name="tavisMovla"),
  path("saponi", views.saponi, name="saponi"),
  path("chusti", views.chusti, name="chusti"),
  path("dispenserebi", views.dispenserebi, name="dispenserebi"),
  path("partniorebi", views.partniorebi, name="partniorebi"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)