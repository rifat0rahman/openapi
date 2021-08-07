from django.db import models

# Create your models here.

class Data(models.Model):
    _id = models.CharField(max_length=1000,default='none',null=True,blank=True)
    id_gara = models.CharField(max_length=1000,default='none',null=True,blank=True)
    criterio_aggiudicazione = models.CharField(max_length=1000,default='none',null=True,blank=True)
    codice_istat_stazione_appaltante = models.CharField(max_length=1000,default='none',null=True,blank=True)
    luogo_esecuzione_nuts = models.CharField(max_length=1000,default='none',null=True,blank=True)
    denominazione_stazione_appaltante = models.CharField(max_length=1000,default='none',null=True,blank=True)
    oggetto_lotto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    imp_lotto_netto_sicurezza = models.CharField(max_length=1000,default='none',null=True,blank=True)
    url_bando = models.TextField(default='none',null=True,blank=True)
    classifica = models.CharField(max_length=1000,default='none',null=True,blank=True)
    data_scadenza_bando = models.CharField(max_length=1000,default='none',null=True,blank=True)
    provincia_stazione_appaltante = models.CharField(max_length=1000,default='none',null=True,blank=True)
    la_sa_agisce_per_conto_di_altro_soggetto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    settore = models.CharField(max_length=1000,default='none',null=True,blank=True)
    numero_gara_anac = models.CharField(max_length=1000,default='none',null=True,blank=True)
    oggetto_della_gara = models.CharField(max_length=1000,default='none',null=True,blank=True)
    categoria_prevalente = models.CharField(max_length=1000,default='none',null=True,blank=True)
    somma_urgenza = models.CharField(max_length=1000,default='none',null=True,blank=True)
    imp_sicurezza = models.CharField(max_length=1000,default='none',null=True,blank=True)
    tipo_procedura = models.CharField(max_length=1000,default='none',null=True,blank=True)
    luogo_esecuzione_istat = models.CharField(max_length=1000,default='none',null=True,blank=True)
    cf_rup = models.CharField(max_length=1000,default='none',null=True,blank=True)
    num_tot_lotti = models.CharField(max_length=1000,default='none',null=True,blank=True)
    nr_lotto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    id_lotto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    data_pubblicazione_scp = models.DateTimeField(auto_now_add=True)
    tipo_appalto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    soggetto_per_cui_agisce_la_sa = models.CharField(max_length=1000,default='none',null=True,blank=True)
    rup = models.CharField(max_length=1000,default='none',null=True,blank=True)
    data_pubblicazione_bando = models.DateTimeField(auto_now_add=True)
    cig = models.CharField(max_length=1000,default='none',null=True,blank=True)
    cup = models.CharField(max_length=1000,default='none',null=True,blank=True)
    modalita_realizzazione = models.CharField(max_length=1000,default='none',null=True,blank=True)
    cpv = models.CharField(max_length=1000,default='none',null=True,blank=True)
    codice_fiscale_stazione_appaltante = models.CharField(max_length=1000,default='none',null=True,blank=True)
    imp_lotto = models.CharField(max_length=1000,default='none',null=True,blank=True)
    importo_gara = models.IntegerField(default=00,null=True,blank=True)
    ufficio = models.CharField(max_length=1000,default='none',null=True,blank=True)
    
    
    #cutom fields
    Bandi_di_Gara = models.FileField(upload_to='files',null=True,blank=True)
    documentazione_aggiuntiva = models.FileField(upload_to='files',null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.id_gara
    




