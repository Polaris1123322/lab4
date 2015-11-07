# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    
    def __unicode__(self):
        return u'%s %s'(self.name, self.country)
class Book(models.Model):
    ISBN = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author_id = models.ForeignKey(Author)
    publisher = models.CharField(max_length=20)
    publish_date  = models.DateField()
    price = models.FloatField()
    
    def __unicode__(self):
        return u'%s %s'(self.title, self.publisher)
        


    
        