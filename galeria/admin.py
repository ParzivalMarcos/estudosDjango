from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")

    ## Deixar os campos como links
    list_display_links = ("id", "nome")

    ## Adicionar campo de busca
    search_fields = ("nome",)

admin.site.register(Fotografia, ListandoFotografias)
