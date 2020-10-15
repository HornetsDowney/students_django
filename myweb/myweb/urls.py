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
    path('admin/', admin.site.urls),
    url(r'^login/', views.login, name='login'),
    url(r'^addr', views.addr, name='addr'),
    url(r'^index/', views.index, name='index'),
    path('', views.index, name='defloud'),
    url('login_action/', views.login_action, name='login_POST') # 只要前台页面提交用户名和密码就可以登陆，还没有进行数据库验证。
]
