from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#ASK;why def doesn't work ?!

class Token(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)


class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User, 'on_delete')
    def __unicode__(self):
        return "{}-{}" .format(self.date,self.amount)

class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount= models.BigIntegerField()
    user = models.ForeignKey(User , 'on_delete')
    def __unicode__(self):
        return "{}-{}".format(self.date,self.amount)	
