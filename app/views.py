# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from random import randint
from .models import Quizz


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'quizzes_list'

    def get_queryset(self):
        return Quizz.objects.all()


class GenerateView(generic.DetailView):
    model = Quizz
    template_name = 'generate.html'

    def get_object(self):
        quizzes_list = Quizz.objects.all()
        length = len(quizzes_list)
        rand_num = randint(1,length-1)
        try:
            quizz = Quizz.objects.get(pk=rand_num)
            return quizz
        except Quizz.DoesNotExist:
            return self.get_object()
