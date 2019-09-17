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


# class Title(models.Model):
#     title = models.CharField(max_length=255)
#     lang = models.CharField(max_length=255)
#     translation = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
#
#
# class Contributor(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Source(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
# class Music(models.Model):
#     iswc = models.CharField(max_length=255, unique=True)
#     titles = models.ManyToManyField(Title)
#     contributors = models.ManyToManyField(Contributor)
#     sources = models.ManyToManyField(Source)
#
#     def __str__(self):
#         return self.iswc



class Title(models.Model):
    title = models.TextField()
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

