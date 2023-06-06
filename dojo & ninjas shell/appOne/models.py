from django.db import models


class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="")
class ninjas(models.Model):
    dojo = models.ForeignKey(dojo, related_name="Dojos", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
# Create your models here.
