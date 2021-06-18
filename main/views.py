import json
import random
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line, Bar, Page, Grid, Scatter
from pyecharts.charts import Tab, Pie, Timeline
from pyecharts import options as opts
from pyecharts.charts.base import Base
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from random import randint


from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import View
from django.db.transaction import atomic

import json
import os
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts

from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import View
from django.db.transaction import atomic

from DITS import settings


class homeView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'home.html')


# class UploadView(APIView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'upload.html')