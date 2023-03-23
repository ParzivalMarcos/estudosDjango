from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")

    ## Deixar os campos como links
    list_display_links = ("id", "nome")

    ## Adicionar campo de busca
    search_fields = ("nome",)

    ## Incluindo filtro por categoria
    list_filter = ("categoria",)

    ## Adicionando paginação
    list_per_page = 10

    ## Habilitar campo para que seja editavel na tela de admin
    list_editable = ("publicada",)

admin.site.register(Fotografia, ListandoFotografias)
