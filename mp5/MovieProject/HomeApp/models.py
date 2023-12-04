from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    details = models.TextField()
    image = models.ImageField(upload_to='Gallery')
    def __str__(self):
        return self.name