# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '14/11/2017 9:44 PM'
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Course
from operation.models import UserFavorite


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


class CourseDetailView(View):
    """
    # 课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            related_courses = Course.objects.filter(tag=tag)[:1]
        else:
            related_courses = []
        return render(request, 'course-detail.html', {
            'course': course,
            'related_courses': related_courses,
            'has_fav_org': has_fav_org,
            'has_fav_course': has_fav_course
        })


class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, 'course-video.html', {
            'course': course,
        })