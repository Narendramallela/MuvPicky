# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name='base.html'
    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        rand_int=random.randint(0,1000);
        some_list=[rand_int,random.randint(0,1000),random.randint(0,1000)]
        context={"bool_var":True,"rand_int":rand_int, "some_list":some_list}
        #print(context)
        return context
