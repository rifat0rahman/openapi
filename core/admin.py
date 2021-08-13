from django.contrib import admin
from .models import Amount, Cig, Data,M_Datas,Stazioni_Appaltanti
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['id_gara','date','provincia_stazione_appaltante','modalita_realizzazione','importo_gara','tipo_appalto','categoria_prevalente','provincia_stazione_appaltante']
    search_fields = ['id_gara','data_pubblicazione_scp','importo_gara']
    list_filter = ['date','tipo_appalto']



class M_dataAdmin(admin.ModelAdmin):
    list_display = ['id_gara','Data_e_ora_apertura_offerte','Location']
    filter_horizontal  = ("Categoria_di_Lavori","Categoria_di_servizi_o_fornitura","Nome_Stazione_Appaltante")




admin.site.register(Data,DataAdmin)
admin.site.register(M_Datas,M_dataAdmin)
admin.site.register(Stazioni_Appaltanti)
admin.site.register(Amount)
admin.site.register(Cig)
