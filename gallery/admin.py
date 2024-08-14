from django.contrib import admin
from .models import Amenitebi, TavisMovla, Saponi, Chusti, Dispenserebi, Partniorebi

class ProductAdmin(admin.ModelAdmin):
  list_display = ('header', 'title',)

# Register your models here.
admin.site.register(Amenitebi, ProductAdmin)
admin.site.register(TavisMovla, ProductAdmin)
admin.site.register(Saponi, ProductAdmin)
admin.site.register(Chusti, ProductAdmin)
admin.site.register(Dispenserebi, ProductAdmin)
admin.site.register(Partniorebi, ProductAdmin)
