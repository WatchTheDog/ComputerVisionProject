import datetime

from django.db import models
from django.utils import timezone


class SearchImage(models.Model):
    imageToSearch = models.ImageField(upload_to='images/')
