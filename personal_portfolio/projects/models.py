from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title
