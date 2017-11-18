# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '14/11/2017 9:44 PM'
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 对课程进行排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)
        paged_courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_courses': paged_courses,
            'sort': sort,
            'hot_courses': hot_courses
        })