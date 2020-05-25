from django.views.generic.list import ListView
from django.shortcuts import render
from import_export import mixins
from django.views.generic.base import View


from . import models


class CategoryExportView(mixins.ExportViewFormMixin, ListView):
    model = models.Category

class Time_api(View):
    """Выводим весь список фильмов(Старый способ)"""
    def get(self, requst):
        routings = models.Book.objects.all()
        return render(requst, "core/multiroute_data_access.html", {'routings_list': routings})