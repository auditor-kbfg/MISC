from django.shortcuts import render , get_list_or_404 , redirect
from .models import USERS
from django.contrib import auth
from django.contrib.auth import authenticate

# Create your views here.

def join(req): # id 와 pw 만 입력 
    if req.method == 'POST':
        id=req.POST["username"]
        pw=req.POST["password"]
        print(id,pw)
        # user=USERS(username=id,password=pw)
        user=USERS.objects.create_user(
            username=id,
            password=pw,
        )
        # auth.lgoin(req,user)
        return redirect('/users/login/')
    else: # get
        return render(req,'users/join.html')

def login(req):
    if req.method=='GET':
        return render(req,'users/login.html')
    elif req.method=='POST':
        id=req.POST.get("user_id")
        pw=req.POST.get("user_pw")
        user=authenticate(req,uesrname=id,password=pw)
        if user is not None:
            auth.login(req,USERS)
            return redirect('/')
        else:
            return redirect('users/join/')

def logout(req):
    auth.logout(req)
    return redirect('/')
