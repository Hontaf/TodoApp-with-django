from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.fields.CharField(max_length=150)
    description = models.fields.TextField(max_length=255)
    #une classe imbriquée :
    class Priority (models.TextChoices):
        Haute = "Haute"
        Moyenne = 'Moyenne'
        Basse = 'Basse'
        Quelconque = "Quelconque"
    priority = models.fields.CharField(choices= Priority.choices,max_length=50)
    enability = models.fields.BooleanField(default= True,null= False)
    date_debut = models.fields.DateField()
    date_expiration = models.fields.DateField()
    to_prolong = models.fields.BooleanField(default=False ,null=True)
        
