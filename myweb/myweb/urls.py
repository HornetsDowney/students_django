"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls), # 注释掉Django自带admin后台
    url('addr', views.addr, name='addr'),  # 登录页面
    url('index/', views.index, name='index'),  # 首页目前闲置，还未使用
    path('', views.login, name='defloud'),  # 设置默认页面为登录页面
    url('user/', views.login_action, name='login_POST'),  # 用户登录
    url('insert/', views.insert, name='insert'),  # 用户注册页面
    # url('secces/', views.select_student, name='student'),  # 设置为登录成功中间页，用于用户页面获取数据库数据
    url('login', views.login, name='login'),
    # url('user/', views.select_student, name='user')
]
