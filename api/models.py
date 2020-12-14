from django.db import models

# Create your models here.
class card(models.Model):
    name = models.CharField(max_length=50)
    card_no  = models.IntegerField()
    expiry = models.DateField()
    cvv = models.IntegerField()

    
