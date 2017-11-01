# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django.db import models

# Create your models here.

class Position(models.Model):
    position = models.CharField(max_length=30)


    def __str__(self):
        return self.position


class Employee(models.Model):
    name = models.CharField(max_length= 30)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices= GENDER)
    dOB = models.DateField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    parents = models.ForeignKey('self', null=True)


    def __str__(self):
        # return "%s %d %d" % (self.name, self.position.id, self.parents)
        return "%s %d" %(self.name, self.position.id)

    def get_absolute_url(self):
        return reverse('subtree', args=[str(self.id)])

    @property
    def get_children(self):
        return Employee.objects.filter(parents=self.id)

