from django.db import models


class Map(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Detour(models.Model):
    map = models.ForeignKey(
        Map, on_delete=models.CASCADE, related_name='detours')
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    notes = models.TextField()

    def __str__(self):
        return self.name
