# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname