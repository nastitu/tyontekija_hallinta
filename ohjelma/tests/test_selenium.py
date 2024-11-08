from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth import get_user_model
import time
from ..models import Maakunta,Kunta, Työpiste, Työntekijä

from django.contrib.auth.models import User

# USER_MODEL = get_user_model()

class TestSelenium(StaticLiveServerTestCase):
    
    def setUp(self):
        
        self.asetukset = webdriver.FirefoxOptions()
        self.selain = webdriver.Firefox(options=self.asetukset)

        self.user1 = User.objects.create_user(
            username='user123',
            password='password456'
        )
        self.user2 = User.objects.create_user(
            username='user234',
            password='password567'
        )
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

    def tearDown(self):
        self.selain.quit()
        

    def test_sisaan_vaihto_ulos_sisaan(self):
        self.selain.get(self.live_server_url)
        #sisäänkirjautumissivulle
        sisaan=self.selain.find_element(By.ID, "nappulaSisaan")
        sisaan.click()
        #täytä tiedot kirjautumissivulla
        nimi=self.selain.find_element(By.ID, "username")
        salasana=self.selain.find_element(By.ID, "password")
        nimi.send_keys("user123")
        salasana.send_keys("password456")
        submit=self.selain.find_element(By.ID, "nappulaSubmit")
        submit.click()

        time.sleep(2)
        # nyt sisällä järjestelmässä
        # vaihdetaan salasana
        valikko=self.selain.find_element(By.ID, "kayttajatili")
        valikko.click()
        salasananVaihto=self.selain.find_element(By.ID, "vaihdaSalasana")
        salasananVaihto.click()
        #nyt vaihtosivulla
        vanha=self.selain.find_element(By.ID, "id_old_password")
        uusi=self.selain.find_element(By.ID, "id_new_password1")
        uudestaan=self.selain.find_element(By.ID, "id_new_password2")
        vanha.send_keys("password456")
        uusi.send_keys("password789")
        uudestaan.send_keys("password789")
        submit=self.selain.find_element(By.ID, "nappulaSubmit")
        submit.click()

        time.sleep(2)

        #kirjaudutaan ulos
        valikko=self.selain.find_element(By.ID, "kayttajatili")
        valikko.click()
        kirjauduUlos=self.selain.find_element(By.ID, "kirjauduUlos")
        kirjauduUlos.click()
        time.sleep(2)
        #kirjaudutaan uudelleen sisään uudella salasanalla
        valikko=self.selain.find_element(By.ID, "kayttajatili")
        valikko.click()
        kirjauduSisaan=self.selain.find_element(By.ID, "kirjauduSisaan")
        kirjauduSisaan.click()
        #täytä tiedot kirjautumissivulla
        nimi=self.selain.find_element(By.ID, "username")
        salasana=self.selain.find_element(By.ID, "password")
        nimi.send_keys("user123")
        salasana.send_keys("password789")
        submit=self.selain.find_element(By.ID, "nappulaSubmit")
        submit.click()

        time.sleep(2)
        #kirjaudutaan ulos


    def test_tyontekijanLisaus(self):
        self.selain.get(self.live_server_url)
        #sisäänkirjautumissivulle
        sisaan=self.selain.find_element(By.ID, "nappulaSisaan")
        sisaan.click()
        #täytä tiedot kirjautumissivulla
        nimi=self.selain.find_element(By.ID, "username")
        salasana=self.selain.find_element(By.ID, "password")
        nimi.send_keys("user234")
        salasana.send_keys("password567")
        submit=self.selain.find_element(By.ID, "nappulaSubmit")
        submit.click()

        time.sleep(2)
        #sisällä, nyt lisäämään
        lisaa=self.selain.find_element(By.ID, "lisaaTyontekija")
        lisaa.click()

        #nyt työntekijän tietojen täyttö
        time.sleep(2)
        enimi=self.selain.find_element(By.ID, "id_etunimi")
        snimi=self.selain.find_element(By.ID, "id_sukunimi")
        puh=self.selain.find_element(By.ID, "id_puhelin")
        email=self.selain.find_element(By.ID, "id_email")
        kosoite=self.selain.find_element(By.ID, "id_katuosoite")
        pnumero=self.selain.find_element(By.ID, "id_postinumero")
        ptpaikka=self.selain.find_element(By.ID, "id_postitoimipaikka")
        aloituspvm=self.selain.find_element(By.ID, "id_aloitus_pvm")
        lopetuspvm=self.selain.find_element(By.ID, "id_lopetus_pvm")
        tsuhde=self.selain.find_element(By.ID, "id_työsuhteen_tyyppi")
        tteht=self.selain.find_element(By.ID, "id_työtehtävä")
        tmkunta=self.selain.find_element(By.ID, "id_työmaakunta")
        tkunta=self.selain.find_element(By.ID, "id_työkunta")
        tpiste=self.selain.find_element(By.ID, "id_työpiste")
        tallenna_nappi=self.selain.find_element(By.LINK_TEXT, "Tallenna")
        enimi.send_keys("Maija")
        snimi.send_keys("Meikäläinen")
        puh.send_keys("123456789")
        email.send_keys("maijam@email.fi")
        kosoite.send_keys("Tammitie 23")
        pnumero.send_keys("12345")
        ptpaikka.send_keys("Helsinki")
        aloituspvm.send_keys("12.12.2024")
        lopetuspvm.send_keys("14.09.2025")
        
        tteht.send_keys("Sihteeri")
        tallenna_nappi.click()

        time.sleep(5)
        self.assertEqual(self.selain.title,'Työntekijähallinta')
