from django.db import models

# Create your models here.
tsuhde=(
    ("vakituinen", "Vakituinen"),
    ("määräaikainen", "Määräaikainen"),
)

class Työntekijä(models.Model):
    etunimi = models.CharField(max_length=50)
    sukunimi = models.CharField(max_length=50)
    puhelin = models.CharField(max_length=50)
    osoite = models.CharField(max_length=100)
    email = models.EmailField()
    aloitus_pvm = models.DateField()
    lopetus_pvm = models.DateField(blank=True,null=True)
    työsuhteen_tyyppi= models.CharField(choices=tsuhde, max_length=50, default="vakituinen")

    def __str__(self):
        return self.sukunimi + ", " + self.etunimi
