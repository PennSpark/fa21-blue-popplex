
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('splash/', views.splash_view, name='splash_view'),
    path('login/', views.login_view, name='login_view'),
    path('signupstudent/', views.signupstudent_view, name='signupstudent_view'),
    path('signupteacher/', views.signupteacher_view, name='signupteacher_view'),
    path('teacherClass/', views.teacherclass_view, name='teacherclass_view'),
    path('teacherpostlecture/', views.teacherpostlecture_view, name='teacherpostlecture_view'),
    path('teacherEnd/', views.teacherEnd_view, name='teacherEnd_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('endclass/', views.endclass_view, name='endclass_view'),
    path('postlecture/', views.postlecture_view, name='postlecture_view'),
    path('delete/', views.delete_view, name='delete_view'),
    path('like/', views.like_tweet, name='like_tweet'),
]
