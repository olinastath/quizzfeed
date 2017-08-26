# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Quizz


# Create your tests here.
def create_quizz(title, subtitle, url, category):
    return Quizz.objects.create(title=title, subtitle=subtitle, url=url, category=category)