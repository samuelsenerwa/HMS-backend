from django.db import models


class User (models.Model):
    firstname = models.CharField(max_length=70, blank=False, default='')
    lastname =  models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=False, default='')
    password = models.CharField(max_length=70, blank=False, default='')