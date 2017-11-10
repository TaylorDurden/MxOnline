# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict
# Create your views here.


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_count = all_orgs.count()
        all_cities = CityDict.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "all_cities": all_cities,
            "org_count": org_count
        })