# Generated by Django 3.2.6 on 2021-08-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_m_datas_data_e_ora_apertura_offerte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_datas',
            name='Location',
            field=models.CharField(blank=True, choices=[('Abruzzo', 'Chieti, L Aquila, Pescara, Teramo.'), ('Basilicata', 'Matera, Potenza.'), ('Calabria', '\tCatanzaro, Cosenza, Crotone, Reggio Calabria, Vibo Valentia.')], max_length=1000, null=True),
        ),
    ]