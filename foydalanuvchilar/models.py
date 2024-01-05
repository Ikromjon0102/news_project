from django.db import models

# Create your models here.
class Foydalanuvchilar(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tyil = models.DateTimeField()
    manzil = models.TextField()

    def __str__(self):
        return f"{self.familiya} {self.ism}"
