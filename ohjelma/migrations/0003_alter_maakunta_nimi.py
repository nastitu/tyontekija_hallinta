# Generated by Django 5.1 on 2024-09-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ohjelma', '0002_alter_maakunta_nimi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maakunta',
            name='nimi',
            field=models.CharField(choices=[('Ahvenanmaa', 'Ahvenanmaa'), ('Etelä-Karjala', 'Etelä-Karjala'), ('Etelä-Pohjanmaa', 'Etelä-Pohjanmaa'), ('Etelä-Savo', 'Etelä-Savo'), ('Kainuu', 'Kainuu'), ('Kanta-Häme', 'Kanta-Häme'), ('Keski-Pohjanmaa', 'Keski-Pohjanmaa'), ('Keski-Suomi', 'Keski-Suomi'), ('Kymenlaakso', 'Kymenlaakso'), ('Lappi', 'Lappi'), ('Pirkanmaa', 'Pirkanmaa'), ('Pohjanmaa', 'Pohjanmaa'), ('Pohjois-Karjala', 'Pohjois-Karjala'), ('Pohjois-Pohjanmaa', 'Pohjois-Pohjanmaa'), ('Pohjois-Savo', 'Pohjois-Savo'), ('Päijät-Häme', 'Päijät-Häme'), ('Satakunta', 'Satakunta'), ('Uusimaa', 'Uusimaa'), ('Varsinais-Suomi', 'Varsinais-Suomi')], max_length=20),
        ),
    ]
