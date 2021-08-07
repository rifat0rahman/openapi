# Generated by Django 3.2.6 on 2021-08-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='_id',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='categoria_prevalente',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='cf_rup',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='cig',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='classifica',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='codice_fiscale_stazione_appaltante',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='codice_istat_stazione_appaltante',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='cpv',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='criterio_aggiudicazione',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='cup',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='data_scadenza_bando',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='denominazione_stazione_appaltante',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='id_gara',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='id_lotto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='imp_lotto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='imp_lotto_netto_sicurezza',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='imp_sicurezza',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='importo_gara',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='la_sa_agisce_per_conto_di_altro_soggetto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='luogo_esecuzione_istat',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='luogo_esecuzione_nuts',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='modalita_realizzazione',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nr_lotto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='num_tot_lotti',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='numero_gara_anac',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='oggetto_della_gara',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='oggetto_lotto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='provincia_stazione_appaltante',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='rup',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='settore',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='soggetto_per_cui_agisce_la_sa',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='somma_urgenza',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='tipo_appalto',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='tipo_procedura',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='ufficio',
            field=models.CharField(blank=True, default='none', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='url_bando',
            field=models.TextField(blank=True, default='none', null=True),
        ),
    ]
