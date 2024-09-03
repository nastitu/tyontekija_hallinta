# Generated by Django 5.1 on 2024-09-03 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0005_alter_kunta_maakunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maakunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(choices=[('ahvenanmaa', 'Ahvenanmaa'), ('etela_karjala', 'Etelä-Karjala'), ('etela_pohjanmaa', 'Etelä-Pohjanmaa'), ('etela_savo', 'Etelä-Savo'), ('kainuu', 'Kainuu'), ('kanta_hame', 'Kanta-Häme'), ('keski_pohjanmaa', 'Keski-Pohjanmaa'), ('keski_suomi', 'Keski-Suomi'), ('kymenlaakso', 'Kymenlaakso'), ('lappi', 'Lappi'), ('pirkanmaa', 'Pirkanmaa'), ('pohjanmaa', 'Pohjanmaa'), ('pohjois_karjala', 'Pohjois-Karjala'), ('pohjois_pohjanmaa', 'Pohjois-Pohjanmaa'), ('pohjois_savo', 'Pohjois-Savo'), ('paijat_hame', 'Päijät-Häme'), ('satakunta', 'Satakunta'), ('uusimaa', 'Uusimaa'), ('varsinais_suomi', 'Varsinais-Suomi')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'maakunnat',
            },
        ),
        migrations.AddField(
            model_name='työntekijä',
            name='työkunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ohjelma.kunta'),
        ),
        migrations.AlterField(
            model_name='työpiste',
            name='kunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ohjelma.kunta'),
        ),
        migrations.AddField(
            model_name='työntekijä',
            name='työmaakunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ohjelma.maakunta'),
        ),
        migrations.AlterField(
            model_name='kunta',
            name='maakunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ohjelma.maakunta'),
        ),
    ]
