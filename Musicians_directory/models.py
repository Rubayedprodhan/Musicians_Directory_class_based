from django.db import models

# Create your models here.
class Musician(models.Model):
   
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email=models.EmailField(max_length=50)
    phone=models.CharField( max_length=11)
    instrument_type =models.CharField( max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
