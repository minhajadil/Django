from django.db import models


# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.type
    