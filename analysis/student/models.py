from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Credential(models.Model):
    name = models.CharField(max_length=200, default=None)
    rollNum = models.CharField(max_length=200, unique=True,default=None)
    dob = models.DateField(default=None)

    def __str__(self):
        return str(self.rollNum)

class Report(models.Model):
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE, default=None)
    mark = models.IntegerField(default=None)

    def __str__(self):
        return str(self.credential)