from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib import auth
from .models import MoveplanUser
# Create your views here.

# 동구 버전 =====
def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['userpassword']
        user = auth.authenticate(request, username=userid, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
    else:    
        return render(request,'login.html')



def signup(request):
    if request.method == "POST":
        if request.POST['userpassword1'] == request.POST['userpassword2']:
            user = MoveplanUser.objects.create_user(request.POST['userid'], password=request.POST['userpassword1'])
            user.ThreeMonthCost = int(request.POST.get('threemonthcost'))
            user.YearPerformance = int(request.POST.get('yearperformance'))
            user.YearAllowance = int(request.POST.get('yearperallowance'))
            user.WorkDays = int(request.POST.get('workdays'))
            user.save()
            auth.login(request, user)
            return redirect('index')
    return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
    