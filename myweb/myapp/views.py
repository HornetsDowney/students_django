from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from myapp import models
from myapp.models import students
from myapp.models import student_info


# Create your views here.
# 登录
def login(request):
    return render(request, 'login.html')


# 首页
def index(request):
    return render(request, 'index.html')


# 用户注册
def addr(request):
    return render(request, 'addr.html')


# 登录模块
def login_action(request):
    context = {}
    login_success = False
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
    else:
        login_success = False
        print('登陆失败')
        context['password'] = '密码错误，请重新输入'
        return render(request, 'login.html', context)
    studentpwd = str(stuser.student_password)
    if pwd == studentpwd:
        login_success = True
        print('登录成功')
        stu = student_info.objects.all()
        if login_success:
            rse = render(request, 'user.html', {'stu': stu})
            rse.set_cookie('username', user, 3600)
            return rse
        # return render(request, 'user.html', {'stu': stu})


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


# 添加学生
@login_required
def insert_student(request):
    if request.method == "POST":
        addr_root = request.POST.get("class_room")
        addr_name = request.POST.get("student_name")
        addr_sex = request.POST.get("student_sex")
        addr_id = request.POST.get("class_id")

        student = student_info(class_root=addr_root, student_name=addr_name, student_sex=addr_sex, student_id=addr_id)
        student.save()
        stu = student_info.objects.all()
    return render(request, 'user.html', {'stu': stu})


# 用户跳转到添加学生信息页面
@login_required
def add_student(request):
    return render(request, 'add_student.html')
