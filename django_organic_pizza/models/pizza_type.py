from django.db import models

class PizzaType(models.Model):
    name = models.CharField(null=False, unique=True, max_length=100)

    def __str__(self):
        return "{}".format(self.name) 
