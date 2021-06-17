from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    last_updated_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Film(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    release_year = models.IntegerField()
    length = models.IntegerField()
    rating = models.IntegerField()
    last_updated_datetime = models.DateTimeField()

    def __str__(self):
        return f"{title} ({release_year})"
