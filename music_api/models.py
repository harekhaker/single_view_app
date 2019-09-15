from django.db import models

# Create your models here.

class Contributor(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Music(models.Model):
    iswc = models.TextField(unique=True)
    song_name = models.TextField()
    contributors = models.ManyToManyField(Contributor)
    providers = models.ManyToManyField(Provider)

    def __str__(self):
        return self.song_name
