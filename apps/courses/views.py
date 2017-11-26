# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '14/11/2017 9:44 PM'
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse

# Create your views here.
from .models import Course, CourseResource
from utils.mixin_utils import LoginRequiredMixin
from operation.models import UserFavorite, UserCourseComments, UserCourse


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


class CourseInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
        all_resources = CourseResource.objects.filter(course=course)

        user_courses = UserCourse.objects.filter(course=course)
        # 取该课程下的所有用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)  # 两个下划线，字段名__in，查询list
        # 取所有相关课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学习过该课程的用户学习的过的相关课程
        related_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        
        return render(request, 'course-video.html', {
            'course': course,
            'all_resources': all_resources,
            'related_courses': related_courses
        })


class CourseCommentView(LoginRequiredMixin, View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_user_comments = UserCourseComments.objects.filter(course=course)
        all_resources = CourseResource.objects.filter(course=course)
        user_courses = UserCourse.objects.filter(course=course)
        # 取该课程下的所有用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids) # 两个下划线，字段名__in，查询list
        # 取所有相关课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学习过该课程的用户学习的过的相关课程
        related_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        return render(request, 'course-comment.html', {
            'course': course,
            'all_user_comments': all_user_comments,
            'all_resources': all_resources,
            'related_courses': related_courses
        })


class UserAddCourseCommentView(View):
    """
    用户添加课程评论信息
    """
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type="application/json")
        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id > 0 and comments:
            course_comments = UserCourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "添加评论成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status": "fail", "msg": "添加评论失败"}', content_type="application/json")