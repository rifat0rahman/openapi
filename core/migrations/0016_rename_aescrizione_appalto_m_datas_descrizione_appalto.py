# Generated by Django 3.2.6 on 2021-08-13 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_m_datas_criterio_di_aggiudizazione'),
    ]

    operations = [
        migrations.RenameField(
            model_name='m_datas',
            old_name='Aescrizione_Appalto',
            new_name='Descrizione_Appalto',
        ),
    ]
