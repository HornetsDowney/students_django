from django.http import HttpResponse
from django.shortcuts import render

from myapp import models
from myapp.models import students


# Create your views here.

def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def addr(request):
    return render(request, 'addr.html')


# 登录模块
def login_action(request):
    context = {}
    if request.method == "POST":
        user = request.POST.get('username', None)  # 避免提交为空时异常
        user = user.strip()  # 去除空格
        pwd = request.POST.get('password', None)
        # 捕获查询不到数据异常，并进行处理
        try:
            stuser = students.objects.get(student_user=user)
        except models.students.DoesNotExist:
            context['usererror'] = '用户名不存在'
            return render(request, 'login.html', context)

        studentpwd = str(stuser.student_password)
        if pwd == studentpwd:
            print('登录成功')
            context['username'] = stuser
            return render(request, 'user.html', context)
    print('登陆失败')
    context['password'] = '密码错误，请重新输入'
    return render(request, 'login.html', context)


# 注册模块
def insert(request):
    if request.method == "POST":
        add_user = request.POST.get('student_user')
        add_pwd = request.POST.get('student_password')
        name = request.POST.get('student_name')
        student = students.objects.filter(student_user=add_user).exists()  # 判断用户输入的账户是否存在
        print(student)
        if student is False:
            print('进入插入学生代码~-------------------------')
            user_data = students(student_user=add_user, student_password=add_pwd, student_name=name)
            user_data.save()
            return render(request, 'login.html')
    return render(request, 'addr.html')
