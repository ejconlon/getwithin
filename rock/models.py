from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=1024)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()

  def __unicode__(self):
    return self.title

class Tag(models.Model):
  slug = models.CharField(max_length=1024)
  body = models.TextField()

  def __unicode__(self):
    return self.slug

class TagSet(models.Model):
  slug = models.CharField(max_length=1024)
  title = models.CharField(max_length=1024)
  tags = models.ManyToManyField(Tag)
  highlighted = models.BooleanField()

  def __unicode__(self):
    return self.title

class Activity(models.Model):
  tag_set = models.ForeignKey(TagSet)
  users = models.ManyToManyField(User)
  slug = models.CharField(max_length=1024)
  title = models.CharField(max_length=1024)
  body = models.TextField()

  def __unicode__(self):
    return self.title
