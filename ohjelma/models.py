from django.db import models

# Create your models here.
tsuhde=(
    ("vakituinen", "Vakituinen"),
    ("määräaikainen", "Määräaikainen"),
)
mkunta= (
        ("Ahvenanmaa", "Ahvenanmaa"),
        ("Etelä-Karjala", "Etelä-Karjala"),
        ("Etelä-Pohjanmaa", "Etelä-Pohjanmaa"),
        ("Etelä-Savo", "Etelä-Savo"),
        ("Kainuu", "Kainuu"),
        ("Kanta-Häme", "Kanta-Häme"),
        ("Keski-Pohjanmaa", "Keski-Pohjanmaa"),
        ("Keski-Suomi", "Keski-Suomi"),
        ("Kymenlaakso", "Kymenlaakso"),
        ("Lappi", "Lappi"),
        ("Pirkanmaa", "Pirkanmaa"),
        ("Pohjanmaa", "Pohjanmaa"),
        ("Pohjois-Karjala", "Pohjois-Karjala"),
        ("Pohjois-Pohjanmaa", "Pohjois-Pohjanmaa"),
        ("Pohjois-Savo", "Pohjois-Savo"),
        ("Päijät-Häme", "Päijät-Häme"),
        ("Satakunta", "Satakunta"),
        ("Uusimaa", "Uusimaa"),
        ("Varsinais-Suomi", "Varsinais-Suomi"),
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
        return self.nimi

    class Meta:
        verbose_name_plural= "kunnat"

class Työpiste(models.Model):
    nimi=models.CharField(max_length=50)
    katuosoite = models.CharField(max_length=100)
    postinumero = models.CharField(max_length=10)
    postitoimipaikka = models.CharField(max_length=50)
    kunta=models.ForeignKey(Kunta, on_delete=models.SET_NULL, null=True, blank= True)

    def __str__(self):
        return self.nimi

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
    työtehtävä = models.CharField(max_length=100)
    työmaakunta=models.ForeignKey(Maakunta, on_delete=models.SET_NULL, null=True, blank= True)
    työkunta= models.ForeignKey(Kunta, on_delete=models.SET_NULL, null=True, blank= True)
    työpiste= models.ForeignKey(Työpiste, on_delete=models.SET_NULL, null=True, blank= True)

    def __str__(self):
        return self.sukunimi + ", " + self.etunimi
    
    class Meta:
        verbose_name_plural= "työntekijät"
