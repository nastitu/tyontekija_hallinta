from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class TestSelenium(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.asetukset = webdriver.FirefoxOptions()
        cls.selain = webdriver.Firefox(options=cls.asetukset)
        
    @classmethod
    def tearDownClass(cls):
        cls.selain.quit()
        super().tearDownClass()

    def test_alku(self):
        self.selain.get(self.live_server_url)

        self.assertEqual(self.selain.title,'Työntekijähallinta')