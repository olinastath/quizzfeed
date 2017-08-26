# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Quizz


# Register your models here.
class QuizzAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'url', 'category']
    list_display = ('title', 'subtitle', 'category')
    search_fields = ['title']

admin.site.register(Quizz, QuizzAdmin)