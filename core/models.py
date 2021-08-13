from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField, create_many_to_many_intermediary_model

# Create your models here.


class Data(models.Model):
    _id = models.CharField(max_length=1000, blank=True,
                           null=True, default='none')
    id_gara = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    criterio_aggiudicazione = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    codice_istat_stazione_appaltante = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    luogo_esecuzione_nuts = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    denominazione_stazione_appaltante = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    oggetto_lotto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    imp_lotto_netto_sicurezza = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    url_bando = models.TextField(default='none', null=True, blank=True)
    classifica = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    data_scadenza_bando = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    provincia_stazione_appaltante = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    la_sa_agisce_per_conto_di_altro_soggetto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    settore = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    numero_gara_anac = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    oggetto_della_gara = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    categoria_prevalente = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    somma_urgenza = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    imp_sicurezza = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    tipo_procedura = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    luogo_esecuzione_istat = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    cf_rup = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    num_tot_lotti = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    nr_lotto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    id_lotto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    data_pubblicazione_scp = models.DateTimeField(auto_now_add=True)
    tipo_appalto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    soggetto_per_cui_agisce_la_sa = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    rup = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    data_pubblicazione_bando = models.DateTimeField(auto_now_add=True)
    cig = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    cup = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    modalita_realizzazione = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    cpv = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    codice_fiscale_stazione_appaltante = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    imp_lotto = models.CharField(
        max_length=1000, default='none', null=True, blank=True)
    importo_gara = models.IntegerField(default=00, null=True, blank=True)
    ufficio = models.CharField(
        max_length=1000, default='none', null=True, blank=True)

    # cutom fields
    Bandi_di_Gara = models.FileField(upload_to='files', null=True, blank=True)
    documentazione_aggiuntiva = models.FileField(
        upload_to='files', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.id_gara



class Categorie(models.Model):
    categorie = models.CharField(max_length=1000,blank=True,null=True)


    def __str__(self) -> str:
        return self.categorie


class Servizi_o_fornitura(models.Model):
    servizi_o_fornitura = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self) -> str:
        return self.servizi_o_fornitura


class Stazioni_Appaltanti(models.Model):
    natura_giuridica_codice = models.CharField(max_length=1000, blank=True, null=True)
    data_inizio = models.CharField(max_length=1000, blank=True, null=True)
    stato = models.CharField(max_length=1000, blank=True, null=True)
    indirizzo_odonimo = models.CharField(max_length=1000, blank=True, null=True)
    data_fine = models.CharField(max_length=1000, blank=True, null=True)
    provincia_codice = models.CharField(max_length=1000, blank=True, null=True)
    citta_nome = models.CharField(max_length=1000, blank=True, null=True)
    flag_inHouse = models.CharField(max_length=1000, blank=True, null=True)
    codice_fiscale = models.CharField(max_length=1000, blank=True, null=True)
    codice_ausa = models.CharField(max_length=1000, blank=True, null=True)
    partita_iva = models.CharField(max_length=1000, blank=True, null=True)
    flag_partecipata = models.CharField(max_length=1000, blank=True, null=True)
    soggetto_estero = models.CharField(max_length=1000, blank=True, null=True)
    denominazione = models.CharField(max_length=1000, blank=True, null=True)
    provincia_nome = models.CharField(max_length=1000, blank=True, null=True)
    citta_codice = models.CharField(max_length=1000, blank=True, null=True)
    cap = models.CharField(max_length=1000, blank=True, null=True)
    natura_giuridica_descrizione = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return self.denominazione

class Amount(models.Model):
    amount = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.amount

class Cig(models.Model):
    cig = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.cig


class M_Datas(models.Model):
    locations = (('Roma', 'Roma'),
                 ('Bari', 'Bari'),
                 ('Udine', 'Udine'),
                 ('Como', 'Como'),
                 ('Lodi', 'Lodi'),
                 ('Asti', 'Asti'),
                 ('Enna', 'Enna'),
                 ('Pisa', 'Pisa'),
                 ('Aosta', 'Aosta'),
                 ('Napoli', 'Napoli'),
                 ('Parma', 'Parma'),
                 ('Rimini', 'Rimini'),
                 ('Latina', 'Latina'),
                 ('Rieti', 'Rieti'),
                 ('Genova', 'Genova'),
                 ('Lecco', 'Lecco'),
                 ('Pavia', 'Pavia'),
                 ('Ancona', 'Ancona'),
                 ('Fermo', 'Fermo'),
                 ('Cuneo', 'Cuneo'),
                 ('Lecce', 'Lecce'),
                 ('Nuoro', 'Nuoro'),
                 ('Arezzo', 'Arezzo'),
                 ('Lucca', 'Lucca'),
                 ('Prato', 'Prato'),
                 ('Siena', 'Siena'),
                 ('Terni', 'Terni'),
                 ('Salerno', 'Salerno'),
                 ('Bologna', 'Bologna'),
                 ('Gorizia', 'Gorizia'),
                 ('Trieste', 'Trieste'),
                 ('Bergamo', 'Bergamo'),
                 ('Milano', 'Milano'),
                 ('Biella', 'Biella'),
                 ('Novara', 'Novara'),
                 ('Torino', 'Torino'),
                 ('Foggia', 'Foggia'),
                 ('Ragusa', 'Ragusa'),
                 ('Bolzano', 'Bolzano'),
                 ('Belluno', 'Belluno'),
                 ('Padova', 'Padova'),
                 ('Rovigo', 'Rovigo'),
                 ('Verona', 'Verona'),
                 ('Avellino', 'Avellino'),
                 ('Caserta', 'Caserta'),
                 ('Ferrara', 'Ferrara'),
                 ('Ravenna', 'Ravenna'),
                 ('Viterbo', 'Viterbo'),
                 ('Imperia', 'Imperia'),
                 ('Savona', 'Savona'),
                 ('Brescia', 'Brescia'),
                 ('Cremona', 'Cremona'),
                 ('Mantova', 'Mantova'),
                 ('Sondrio', 'Sondrio'),
                 ('Varese.', 'Varese.'),
                 ('Taranto', 'Taranto'),
                 ('Cagliari', 'Cagliari'),
                 ('Sassari', 'Sassari'),
                 ('Catania', 'Catania'),
                 ('Messina', 'Messina'),
                 ('Palermo', 'Palermo'),
                 ('Trapani', 'Trapani'),
                 ('Firenze', 'Firenze'),
                 ('Livorno', 'Livorno'),
                 ('Pistoia', 'Pistoia'),
                 ('Treviso', 'Treviso'),
                 ('Venezia', 'Venezia'),
                 ('Vicenza', 'Vicenza'),
                 ('Piacenza', 'Piacenza'),
                 ('Pordenone', 'Pordenon'),
                 ('Frosinone', 'Frosinon'),
                 ('Macerata', 'Macerata'),
                 ('Isernia.', 'Isernia.'),
                 ('Vercelli', 'Vercelli'),
                 ('Brindisi', 'Brindisi'),
                 ('Oristano', 'Oristano'),
                 ('Agrigento', 'Agrigento'),
                 ('Siracusa', 'Siracusa'),
                 ('Grosseto', 'Grosseto'),
                 ('Benevento', 'Benevento'),
                 ('La Spezia', 'La Spezia'),
                 ('Campobasso', 'Campobasso'),
                 ('Alessandria', 'Alessandria'),
                 ('Forlì-Cesena', 'Forlì-Cesen'),
                 ('Reggio Emilia', 'Reggio Emilia'),
                 ('Sud Sardegna', 'Sud Sardegna'),
                 ('Ascoli Piceno', 'Ascoli Piceno'),
                 ('Caltanissetta', 'Caltanissetta'),
                 ('Massa-Carrara', 'Massa-Carrara'),
                 ('Pesaro Urbino.', 'Pesaro Urbino.'),
                 ('Trento Perugia', 'Trento Perugia'),
                 ('Verbano-Cusio-Ossola', 'Verbano-Cusio-Ossola'),
                 ('Monza e della Brianza', 'Monza e della Brianza'),
                 ('Barletta-Andria-Trani', 'Barletta-Andria-Trani'))

    tipologia_di_Appalto = (
        ('Lavori','Lavori'),
        ('Servizi','Servizi'),
        ('Forniture','Forniture'),
    )

    criterio = (
        ("Offerta economicamente più Vantaggiosa","Offerta economicamente più Vantaggiosa"),
        ("Minor Presso","Minor Presso"),
        ("Prezzo Più Basso","Prezzo Più Basso")
    )

    id_gara = models.CharField(max_length=1000, blank=True, null=True)

    website = models.CharField(max_length=1000, blank=True, null=True)

    cig = models.ManyToManyField(Cig)

    Descrizione_Appalto = models.CharField(
        max_length=1000, blank=True, null=True)

    Tipologia_di_Appalto = models.CharField(choices=tipologia_di_Appalto,max_length=1000, blank=True, null=True)

    ammount = models.ManyToManyField(Amount)

    Criterio_di_aggiudizazione = models.CharField(choices=criterio,max_length=1000, blank=True, null=True)

    Scadenza_ricezione_Offerte = models.CharField(
        max_length=1000, blank=True, null=True)

    Data_e_ora_apertura_offerte = models.DateTimeField(blank=True, null=True)
    rup = models.CharField(max_length=1000, blank=True, null=True)

    Nome_Stazione_Appaltante = models.ManyToManyField(Stazioni_Appaltanti)

    Location = models.CharField(
        choices=locations, max_length=1000, blank=True, null=True)

    Categoria_di_servizi_o_fornitura = models.ManyToManyField(Servizi_o_fornitura)

    Categoria_di_Lavori = models.ManyToManyField(Categorie)

    Attachment_file = models.FileField(
        upload_to='files', max_length=100, blank=True, null=True)

    Other_attachment_file = models.FileField(
        upload_to='files', max_length=100, blank=True, null=True)


