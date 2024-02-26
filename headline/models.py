from django.db import models

# Create your models here.
class NewsMod (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    image = models.CharField(max_length=255, null = True, blank = True)

    def __str__(self):
        return self.title