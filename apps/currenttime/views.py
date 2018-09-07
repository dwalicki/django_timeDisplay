# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {
        "time": datetime.now()
    }
    return render(request,'currenttime/index.html', context)
