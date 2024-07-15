from django.contrib import admin
from .models import MyariSaponi, Tsubi, PetBotli,Chusti,Dispenserebi,EliteAlternative

class ProductAdmin(admin.ModelAdmin):
  list_display = ('header', 'title',)

# Register your models here.
admin.site.register(MyariSaponi, ProductAdmin)
admin.site.register(Tsubi, ProductAdmin)
admin.site.register(PetBotli, ProductAdmin)
admin.site.register(Chusti, ProductAdmin)
admin.site.register(Dispenserebi, ProductAdmin)
admin.site.register(EliteAlternative, ProductAdmin)
