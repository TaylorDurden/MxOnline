# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '30/10/2017 10:51 PM'


import xadmin

from . import models


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_num']
    list_filter = ['name', 'desc', 'click_num', 'fav_num', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


xadmin.site.register(models.CityDict, CityDictAdmin)
xadmin.site.register(models.CourseOrg, CourseOrgAdmin)
xadmin.site.register(models.Teacher, TeacherAdmin)
