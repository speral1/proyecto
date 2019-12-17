from django.db import models

# Create your models here.

# Modelo pizza
class pizza(models.Model):

    # nombre pizza
    nombreP = models.CharField(max_length=128, unique=True)


# Modelo ingrediente
class ingrediente(models.Model):

    # nombre ingrediente
    nombreI = models.CharField(max_length=128, unique=True)

# modelo contiene
class contiene(models.Model):

    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE, null=False)
    ingrediente = models.ForeignKey(ingrediente, on_delete=models.CASCADE, null=False)
    porcentaje = models.DecimalField(decimal_places=3, max_digits=10)
