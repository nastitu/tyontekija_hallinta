from django.test import TestCase
from ..models import Maakunta,Kunta, Työpiste, Työntekijä
import datetime


class TestModels(TestCase):
    def setUp(self):
        self.maakunta1=Maakunta.objects.create(nimi="Uusimaa")
        self.maakunta2=Maakunta.objects.create(nimi="Satakunta")
        self.kunta1=Kunta.objects.create(maakunta=self.maakunta1, nimi="Helsinki")
        self.kunta2=Kunta.objects.create(maakunta=self.maakunta1, nimi="Vantaa")
        self.kunta3=Kunta.objects.create(maakunta=self.maakunta2, nimi="Pori")
        self.tyopiste1=Työpiste.objects.create(
            nimi="Piste1",
            katuosoite="Katu 1",
            postinumero = "12345",
            postitoimipaikka = "Helsinki",
            kunta= self.kunta1
        )
        self.tyopiste2=Työpiste.objects.create(
            nimi="Piste2",
            katuosoite="Kuja 2",
            postinumero = "23456",
            postitoimipaikka = "Pori",
            kunta= self.kunta3
        )
        self.tyopiste3=Työpiste.objects.create(
            nimi="Piste3",
            katuosoite="Kuja 3",
            postinumero = "34567",
            postitoimipaikka = "Vantaa",
            kunta= self.kunta2
        )
        self.tyontekija1=Työntekijä.objects.create(
            etunimi="Etunimi1",
            sukunimi="Sukunimi1",
            puhelin = "123456789",
            email = "email@email.fi",
            katuosoite = "Tie 23",
            postinumero = "45678",
            postitoimipaikka = "Espoo",
            aloitus_pvm = datetime.date(2023, 9, 10),
            työtehtävä = "sihteeri"
        )
        self.tyontekija2=Työntekijä.objects.create(
            etunimi="Etunimi2",
            sukunimi="Sukunimi2",
            puhelin = "23456789",
            email = "email2@email.fi",
            katuosoite = "Kuja 45",
            postinumero = "45678",
            postitoimipaikka = "Helsinki",
            aloitus_pvm = datetime.date(2023, 9, 10),
            lopetus_pvm = datetime.date(2025, 7, 12),
            työsuhteen_tyyppi= "määräaikainen",
            työtehtävä = "johtaja",
            työmaakunta=self.maakunta1,
            työkunta= self.kunta1,
            työpiste= self.tyopiste1
        )

    def test_str(self):
        ''' Testaa __str__ '''

        self.assertEqual(str(self.maakunta1), "Uusimaa")
        self.assertEqual(str(self.maakunta2), "Satakunta")
        self.assertEqual(str(self.kunta1), "Helsinki")
        self.assertEqual(str(self.kunta2), "Vantaa")
        self.assertEqual(str(self.kunta3), "Pori")
        self.assertEqual(str(self.tyopiste1), "Piste1")
        self.assertEqual(str(self.tyopiste2), "Piste2")
        self.assertEqual(str(self.tyopiste3), "Piste3")
        self.assertEqual(str(self.tyontekija1), "Sukunimi1, Etunimi1")
        self.assertEqual(str(self.tyontekija2), "Sukunimi2, Etunimi2")

    def test_tyosuhteen_tyyppi(self):
        ''' Testaa työsuhteen tyypin '''

        self.assertEqual(self.tyontekija1.työsuhteen_tyyppi, "vakituinen")
        self.assertEqual(self.tyontekija2.työsuhteen_tyyppi, "määräaikainen")
    
    def test_null_arvot(self):
        ''' Testaa null arvot työntekijällä'''

        self.assertIsNone(self.tyontekija1.lopetus_pvm)
        self.assertIsNone(self.tyontekija1.työmaakunta)
        self.assertIsNone(self.tyontekija1.työkunta)
        self.assertIsNone(self.tyontekija1.työpiste)
    
