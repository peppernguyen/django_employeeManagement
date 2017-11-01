# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Position, Employee
# Register your models here.
admin.site.register(Position)
admin.site.register(Employee)