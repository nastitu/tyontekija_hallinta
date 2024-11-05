from django.test import TestCase
from ..models import Maakunta,Kunta, Työpiste, Työntekijä
import datetime
from django.urls import reverse
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()
# Create your tests here.


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create_user(
            username='user123',
            password='password456'
        )

    # def setUp(self):
    #     self.user = USER_MODEL.objects.create_user(
    #         username='user123',
    #         password='password456'
    #     )
    
    def test_index(self):
        '''Testaa että aloitus toimii'''
        url=reverse('index')
        response=self.client.get(url)

        self.assertEqual(response.status_code,200)

    def test_lisaa_tyontekija(self):
        '''Testaa että lisäys toimii kun logattuna sisään'''
        self.client.force_login(self.user)

        url=reverse('lisaa_t')
        response=self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'tyontekija.html')

    def test_kirjauduttuna_ulos_lisays(self):
        '''Testaa että kun logattuna ulos, niin lisäys ei onnistu vaan
        uudelleenohjaa'''
        url=reverse('lisaa_t')
        response=self.client.get(url)

        self.assertEqual(response.status_code,302)
        
    def test_muokkaa_tyontekijaa(self):
        pass

    def test_poista_tyontekija(self):
        pass

