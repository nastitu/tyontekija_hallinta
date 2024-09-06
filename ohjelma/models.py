from django.db import models

# Create your models here.
tsuhde=(
    ("vakituinen", "Vakituinen"),
    ("määräaikainen", "Määräaikainen"),
)
mkunta= (
        ('ahvenanmaa', 'Ahvenanmaa'),
        ('etela_karjala', 'Etelä-Karjala'),
        ('etela_pohjanmaa', 'Etelä-Pohjanmaa'),
        ('etela_savo', 'Etelä-Savo'),
        ('kainuu', 'Kainuu'),
        ('kanta_hame', 'Kanta-Häme'),
        ('keski_pohjanmaa', 'Keski-Pohjanmaa'),
        ('keski_suomi', 'Keski-Suomi'),
        ('kymenlaakso', 'Kymenlaakso'),
        ('lappi', 'Lappi'),
        ('pirkanmaa', 'Pirkanmaa'),
        ('pohjanmaa', 'Pohjanmaa'),
        ('pohjois_karjala', 'Pohjois-Karjala'),
        ('pohjois_pohjanmaa', 'Pohjois-Pohjanmaa'),
        ('pohjois_savo', 'Pohjois-Savo'),
        ('paijat_hame', 'Päijät-Häme'),
        ('satakunta', 'Satakunta'),
        ('uusimaa', 'Uusimaa'),
        ('varsinais_suomi', 'Varsinais-Suomi'),
)
class Maakunta(models.Model):
    nimi=models.CharField(choices=mkunta, max_length=20)#  default='uusimaa')

    def __str__(self):
        return self.nimi

    class Meta:
        verbose_name_plural= "maakunnat"

class Kunta(models.Model):
    maakunta=models.ForeignKey(Maakunta, on_delete=models.SET_NULL, null=True, blank= True)
    nimi=models.CharField(max_length=50)
    

    def __str__(self):
        return self.maakunta.nimi + ": " + self.nimi

    class Meta:
        verbose_name_plural= "kunnat"

class Työpiste(models.Model):
    nimi=models.CharField(max_length=50)
    katuosoite = models.CharField(max_length=100)
    postinumero = models.CharField(max_length=10)
    postitoimipaikka = models.CharField(max_length=50)
    kunta=models.ForeignKey(Kunta, on_delete=models.SET_NULL, null=True, blank= True)

    def __str__(self):
        return self.kunta.nimi + ": " + self.nimi

    class Meta:
        verbose_name_plural= "työpisteet"


class Työntekijä(models.Model):
    etunimi = models.CharField(max_length=50)
    sukunimi = models.CharField(max_length=50)
    puhelin = models.CharField(max_length=50)
    email = models.EmailField()
    katuosoite = models.CharField(max_length=100)
    postinumero = models.CharField(max_length=10)
    postitoimipaikka = models.CharField(max_length=50)
    aloitus_pvm = models.DateField()
    lopetus_pvm = models.DateField(blank=True,null=True)
    työsuhteen_tyyppi= models.CharField(choices=tsuhde, max_length=50, default="vakituinen")
    työmaakunta=models.ForeignKey(Maakunta, on_delete=models.SET_NULL, null=True, blank= True)
    työkunta= models.ForeignKey(Kunta, on_delete=models.SET_NULL, null=True, blank= True)
    työpiste= models.ForeignKey(Työpiste, on_delete=models.SET_NULL, null=True, blank= True)

    def __str__(self):
        return self.sukunimi + ", " + self.etunimi
    
    class Meta:
        verbose_name_plural= "työntekijät"
