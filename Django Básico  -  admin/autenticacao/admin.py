from django.contrib import admin
from .models import Pessoa, Cargos, Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse

class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome', 'quantidade', 'descricao')
    list_display = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 0 

@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions ,admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ('get_foto', 'nome_completo', 'email', 'senha')
    #readonly_fields = ('cargo',)
    search_fields = ('nome', )
    list_filter = ('cargo',)
    list_editable = ('email',)

    def mostra_pessoa(self, request, pessoa):
        return HttpResponse(pessoa)
        
    mostra_pessoa.label = 'Mostra pessoa'
    change_actions = ("mostra_pessoa",)

admin.site.register(Cargos)
