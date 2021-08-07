from rest_framework import serializers
from .models import Data


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
