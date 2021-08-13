# Generated by Django 3.2.6 on 2021-08-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_m_datas_categoria_di_lavori'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servizi_o_fornitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servizi_o_fornitura', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='m_datas',
            name='Categoria_di_servizi_o_fornitura',
        ),
        migrations.AddField(
            model_name='m_datas',
            name='Categoria_di_servizi_o_fornitura',
            field=models.ManyToManyField(to='core.Servizi_o_fornitura'),
        ),
    ]
