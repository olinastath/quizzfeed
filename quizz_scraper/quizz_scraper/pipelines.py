# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from app.models import Quizz


class QuizzScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            duplicate = Quizz.objects.get(title=item["title"])
            return item
        except Quizz.DoesNotExist:
            pass

        item.save()
        return item
