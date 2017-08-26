# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from app.models import Quizz
from scrapy_djangoitem import DjangoItem


class QuizzItem(DjangoItem):
    django_model = Quizz

    for item in Quizz.objects.all():
        if Quizz.objects.filter(title=item.title).count() > 1:
            item.delete()
