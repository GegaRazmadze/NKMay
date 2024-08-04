

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
  path('admin', admin.site.urls),
  path('', views.index, name="index"),
  path("tsubi", views.tsubi, name="tsubi"),
  path("petBotli", views.petBotli, name="petBotli"),
  path("chusti", views.chusti, name="chusti"),
  path("dispenserebi", views.dispenserebi, name="dispenserebi"),
  path("eliteAlternative", views.eliteAlternative, name="eliteAlternative"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)