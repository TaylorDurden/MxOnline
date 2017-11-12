# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

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

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)
        paged_orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": paged_orgs,
            "all_cities": all_cities,
            "org_count": org_count
        })