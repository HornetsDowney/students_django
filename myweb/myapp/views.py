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
            return render(request, 'user.html')

    print('登陆失败')
    return render(request, 'login.html')
