from django.contrib import admin
from .models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['id_gara','date','provincia_stazione_appaltante','modalita_realizzazione','importo_gara','tipo_appalto','categoria_prevalente','provincia_stazione_appaltante']
    search_fields = ['id_gara','data_pubblicazione_scp','importo_gara']
    list_filter = ['date','tipo_appalto']


admin.site.register(Data,DataAdmin)