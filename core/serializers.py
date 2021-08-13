
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Data, M_Datas, Stazioni_Appaltanti


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = (
             'criterio_aggiudicazione', 'codice_istat_stazione_appaltante', 'luogo_esecuzione_nuts', 'denominazione_stazione_appaltante', 'oggetto_lotto', 
            'imp_lotto_netto_sicurezza', 'url_bando', 'classifica', 'data_scadenza_bando', 'provincia_stazione_appaltante', 'settore', 'la_sa_agisce_per_conto_di_altro_soggetto', 
            'numero_gara_anac', 'oggetto_della_gara', 'categoria_prevalente', 'somma_urgenza', 'imp_sicurezza', 'tipo_procedura', 'luogo_esecuzione_istat', 'cf_rup', 
            'num_tot_lotti', 'nr_lotto', 'id_lotto', 'data_pubblicazione_scp', 'tipo_appalto', 'soggetto_per_cui_agisce_la_sa', 'rup', 'data_pubblicazione_bando', 
            'cig', 'cup', 'modalita_realizzazione', 'cpv', 'codice_fiscale_stazione_appaltante', 'imp_lotto', 'id_gara', '_id', 'importo_gara', 'ufficio',
            'Bandi_di_Gara','documentazione_aggiuntiva','id'
        )

class MdataSerializer(serializers.ModelSerializer):
    class Meta:
        # Categoria_di_servizi_o_fornitura = serializers.CharField(source="")
        model = M_Datas
        fields = (
            "id_gara","website","cig","Descrizione_Appalto","Tipologia_di_Appalto",
            "ammount","Criterio_di_aggiudizazione","Scadenza_ricezione_Offerte","Data_e_ora_apertura_offerte",
            "rup","Location","Attachment_file","Other_attachment_file","Nome_Stazione_Appaltante",
            "Categoria_di_servizi_o_fornitura","Categoria_di_Lavori"
        )
        depth = 1

class StazioniSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stazioni_Appaltanti
        fields = '__all__'
