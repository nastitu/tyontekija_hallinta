# Generated by Django 5.1 on 2024-09-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maakunta',
            name='nimi',
            field=models.CharField(choices=[('ahvenanmaa', 'Ahvenanmaa'), ('etela_karjala', 'Etelä-Karjala'), ('etela_pohjanmaa', 'Etelä-Pohjanmaa'), ('etela_savo', 'Etelä-Savo'), ('kainuu', 'Kainuu'), ('kanta_hame', 'Kanta-Häme'), ('keski_pohjanmaa', 'Keski-Pohjanmaa'), ('keski_suomi', 'Keski-Suomi'), ('kymenlaakso', 'Kymenlaakso'), ('lappi', 'Lappi'), ('pirkanmaa', 'Pirkanmaa'), ('pohjanmaa', 'Pohjanmaa'), ('pohjois_karjala', 'Pohjois-Karjala'), ('pohjois_pohjanmaa', 'Pohjois-Pohjanmaa'), ('pohjois_savo', 'Pohjois-Savo'), ('paijat_hame', 'Päijät-Häme'), ('satakunta', 'Satakunta'), ('uusimaa', 'Uusimaa'), ('varsinais_suomi', 'Varsinais-Suomi')], max_length=20),
        ),
    ]
