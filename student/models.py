from django.db import models

# Create your models here.
class Student_table(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    number=models.IntegerField(blank=True, null=True)

def __str__(self):
     return f"{self.first_name}- {self.last_name}"