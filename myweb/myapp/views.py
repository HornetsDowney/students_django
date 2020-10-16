from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import students


# Create your views here.

def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def addr(request):
    return render(request, 'addr.html')


def login_action(request):
    if request.method == "POST":
        user = request.POST.get('username', None)  # 避免提交为空时异常
        user = user.strip()  # 去除空格
        pwd = request.POST.get('password', None)
        stuser = students.objects.get(student_user=user)
        studentpwd = str(stuser.student_password)
        if pwd == studentpwd:
            print(user)
            print(pwd)
            print('登录成功')
            return render(request, 'user.html')

    print('登陆失败')
    return render(request, 'login.html')


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
