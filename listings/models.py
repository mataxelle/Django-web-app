from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Brand(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Country(models.TextChoices):
        France = 'France'
        Espagne = 'Espagne'
        Japon = 'Japon'
        Coree_du_sud = 'Corée du sud'
        USA = 'Étas-Unis'
        Mexique = 'Mexique'
        Autre = 'Autre'
    
    class MerchType(models.TextChoices):
        Vêtement = 'Vêtement'
        Chaussure = 'Chaussure'
        Poster = 'Poster'
        Divers = 'Divers'

    name = models.fields.CharField(max_length=100)
    country = models.fields.CharField(max_length=100, choices=Country.choices)
    biography = models.fields.CharField(max_length=1000)
    year_created = models.fields.IntegerField(validators=[MinValueValidator(1850), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    creator = models.fields.CharField(max_length=100, null=True, blank=True)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1850), MaxValueValidator(2024)])
    type = models.fields.CharField(max_length=100, choices=MerchType.choices)

