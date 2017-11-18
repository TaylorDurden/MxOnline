# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '14/11/2017 9:44 PM'

from django.conf.urls import url, include


from .views import CourseListView


urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="org_list"),
]