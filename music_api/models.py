from django.db import models

# Create your models here.

# from django.db.models import Func
#
# class Levenshtein(Func):
#     template = "%(function)s(%(expressions)s, '%(search_term)s')"
#     function = "levenshtein"
#
#     def __init__(self, expression, search_term, **extras):
#         super(Levenshtein, self).__init__(
#             expression,
#             search_term=search_term,
#             **extras
#         )

class Contributor(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    iswc = models.TextField(unique=True)
    song_name = models.TextField()
    contributors = models.ManyToManyField(Contributor)
    providers = models.ManyToManyField(Provider)

    def __str__(self):
        return self.song_name
