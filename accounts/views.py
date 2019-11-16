from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
#회원가입함수
def signup(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        pworigin = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        if pworigin != passwordConfirm:
            # return render(request,'signup.html',{"error":"비밀번호가 맞지 않습니다."})
            try:#밑에 조건문을 실행을 시켜라 실행되면 하고 안되면 except문을 실행  시켜라
                user = User.objects.get(username=request.POST['userId'])
                return render(request, 'signup.html',{'error': 'Username has already been taken'})
            except User.DoesNotExist:              
                user = User.objects.create_user(userId,password=pworigin)
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request,'signup.html',{'error': 'Passwords must match'})
    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method == 'POST':
        UserId = request.POST['userId']
        Pworigin= request.POST['password']
        user = auth.authenticate(request, username= userId, password=password)#authenticate 인증,있는지 없는지
        if user is not None: #True,False None-데이터 있냐 없냐를 물어보는 것.
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    else:
        return render(request,'index')
