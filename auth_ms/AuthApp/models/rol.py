from django.db import models;

class Rol (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name',max_length=100, unique=True)
    description = models.CharField('description',max_length=100)