from django.db import models


class Title(models.Model):
    title = models.TextField(unique=True)
    lang = models.TextField()
    translation = models.TextField()

    def __str__(self):
        return self.title


class Contributor(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    iswc = models.TextField(unique=True)
    titles = models.ManyToManyField(Title)
    contributors = models.ManyToManyField(Contributor)
    sources = models.ManyToManyField(Source)

    def __str__(self):
        return self.iswc



