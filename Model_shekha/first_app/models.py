from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=20)
    Roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name =models.TextField()

    def __str__(self):
        return f'{self.Name} -{self.Roll}'


