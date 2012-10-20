from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
