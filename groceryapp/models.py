from django.db import models


# Create your models here.
VISIBILITY_CHOICES = (
    ("PENDING", "PENDING"),
    ("NOT AVAILABLE", "NOT AVAILABLE"),
    ("BOUGHT", "BOUGHT")
)


class Grocery(models.Model):
    name = models.CharField(max_length=500)
    quantity = models.CharField(max_length=500)
    status =  models.CharField(max_length=100,
                             choices=VISIBILITY_CHOICES,
                             default=VISIBILITY_CHOICES[0][0])
    added_date = models.DateField()

