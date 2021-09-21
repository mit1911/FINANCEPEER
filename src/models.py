from django.db import models


# Create your models here.

class Data(models.Model):
    userId = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
