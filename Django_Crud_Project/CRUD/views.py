# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views her
def index(request):
    return render(request, 'index.htme')

