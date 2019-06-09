from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='favorites')
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    notes = models.TextField()

    def __str__(self):
        return self.name
