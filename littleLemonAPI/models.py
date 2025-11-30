from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name= models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    inventory= models.IntegerField()
    def get_item(self):
        return f'{self.name}: {self.price}'