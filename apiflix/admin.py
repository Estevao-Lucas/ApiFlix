from django.contrib import admin
from apiflix.models import Programa

# Register your models here.
class Programas(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tipo', 'data_lancamento')
    list_display_links = ('id', 'titulo')
    list_per_page = 10

admin.site.register(Programa, Programas)
