from django.db import models


class Post(models.Model):
    cover = models.ImageField(upload_to='images/')

