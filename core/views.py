from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .serializers import DataSerializer, MdataSerializer, StazioniSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from .models import Categorie, Data, M_Datas, Servizi_o_fornitura, Stazioni_Appaltanti
import time
# for continius calling the funtion
# Create your views here.
import sched
import time


@api_view(['GET', 'POST'])
def home(request):
    table_data = Data.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(table_data, request)
    serializers = DataSerializer(result_page, many=True)
    run_every_day()

    return paginator.get_paginated_response(serializers.data)


def run_every_day():
    user_agent_desktop = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
        'Safari/537.36'
    headers = {'User-Agent': user_agent_desktop}
    url = 'http://dati.mit.gov.it/catalog/api/action/datastore_search?resource_id=445c4413-f5cc-4f08-a02e-66accb249dc0&limit=100'
    data = requests.get(url, headers=headers)
    data.raise_for_status()
    data = data.json()

    fields = data['result']['records']

    for field in fields:
        table, created = Data.objects.get_or_create(
            criterio_aggiudicazione=field["criterio_aggiudicazione"],
            codice_istat_stazione_appaltante=field["codice_istat_stazione_appaltante"],
            luogo_esecuzione_nuts=field["luogo_esecuzione_nuts"],
            denominazione_stazione_appaltante=field["denominazione_stazione_appaltante"],
            oggetto_lotto=field["oggetto_lotto"],
            imp_lotto_netto_sicurezza=field["imp_lotto_netto_sicurezza"],
            url_bando=field["url_bando"],
            data_scadenza_bando=field["data_scadenza_bando"],
            provincia_stazione_appaltante=field["provincia_stazione_appaltante"],
            settore=field["settore"],
            la_sa_agisce_per_conto_di_altro_soggetto=field["la_sa_agisce_per_conto_di_altro_soggetto"],
            numero_gara_anac=field["numero_gara_anac"],
            oggetto_della_gara=field["oggetto_della_gara"],
            categoria_prevalente=field["categoria_prevalente"],
            somma_urgenza=field["somma_urgenza"],
            imp_sicurezza=field["imp_sicurezza"],
            tipo_procedura=field["tipo_procedura"],
            luogo_esecuzione_istat=field["luogo_esecuzione_istat"],
            cf_rup=field["cf_rup"],
            num_tot_lotti=field["num_tot_lotti"],
            nr_lotto=field["nr_lotto"],
            id_lotto=field["id_lotto"],
            tipo_appalto=field["tipo_appalto"],
            soggetto_per_cui_agisce_la_sa=field["soggetto_per_cui_agisce_la_sa"],
            rup=field["rup"],
            data_pubblicazione_bando=field["data_pubblicazione_bando"],
            cig=field["cig"],
            cup=field["cup"],
            modalita_realizzazione=field["modalita_realizzazione"],
            cpv=field["cpv"],
            codice_fiscale_stazione_appaltante=field["codice_fiscale_stazione_appaltante"],
            imp_lotto=field["imp_lotto"],
            id_gara=field["id_gara"],
            _id=field["_id"],
            importo_gara=float(field["importo_gara"]),
            ufficio=field["ufficio"]
        )
        table.save()

run_every_day()

# run the app
import datetime as dt
from threading import Timer

def my_job():
    run_every_day()


nextDay = dt.datetime.now() + dt.timedelta(days=1)
dateString = nextDay.strftime('%d-%m-%Y') + " 01-00-00"
newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
delay = (newDate - dt.datetime.now()).total_seconds()
Timer(delay,my_job,()).start()


# new m-data

@api_view(['GET'])
def m_data(request):
    mdata = M_Datas.objects.all()
    serializers = MdataSerializer(mdata,many=True)
    return Response(serializers.data)




@api_view(['GET'])
def stazioni_appaltanti(request):
    stazioni = Stazioni_Appaltanti.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 20
    result_page = paginator.paginate_queryset(stazioni, request)
    serializers = StazioniSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializers.data)