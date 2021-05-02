from django.urls import path
from . import views,urls

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register',views.register, name = 'register'),
    path('studreg',views.studreg, name = 'studreg'),
    path('teacherlogin',views.teacherlogin, name = 'teacherlogin'),
    path('studlogin',views.studlogin, name = 'studlogin'),
    path('logout',views.logout, name = 'logout'),
    path('teacher_dash',views.teacher_dash, name = 'teacher_dash'),
    path('testdash',views.testdash, name = 'testdash'),
    path('newtest',views.newtest, name = 'newtest'),
    path('createtest',views.createtest, name = 'createtest'),
    path('announ',views.announ, name = 'announ'),
    path('createannoun',views.createannoun, name = 'createannoun'),
    path('stud_dash',views.stud_dash, name = 'stud_dash'),
    path('viewannoun',views.viewannoun, name = 'viewannoun'),
    path('pendtest',views.pendtest, name = 'pendtest'),
    path('test',views.test, name = 'test'),
    path('pre',views.pre, name = 'pre'),
    path('post',views.post, name = 'post'),
    path('feed',views.feed, name = 'feed'),
    path('addresc',views.addresc, name = 'addresc'),
    path('viewresc',views.viewresc, name = 'viewresc'),

    path('postannou',views.postannou,name='postannou'),
]