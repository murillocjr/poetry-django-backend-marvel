from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    year_published = models.PositiveSmallIntegerField()


class LoginRequestDTO(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
