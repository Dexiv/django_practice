from django.db import models

class Kartoshka(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
