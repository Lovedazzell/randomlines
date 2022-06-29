from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect
from . forms import Registration, User_login, password_change
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Dashboard.
def dashboard(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        lname = request.user.last_name
    else:
        fname =""
        lname = ""
    contex = {"fname":fname, "lname":lname}
    return render(request,'main/home.html',contex)


# Vedio content.
def video(request):
    contex = {}
    return render(request,'main/video.html',contex)


# Login page.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = User_login(request = request ,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                udata = authenticate(username = uname, password = upass)
                if udata is not None:
                    login(request, udata)
                    return HttpResponseRedirect("/home/")
        else:
            form = User_login()
        contex = {"forms":form}
        return render(request,'main/login.html',contex)
    else:
        return HttpResponseRedirect("/home/")


# Sing Up.
def singup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = Registration(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/login/")
        else:
            fm = Registration()
        contex = {"fm":fm}
        return render(request,'main/singup.html',contex)
    else:
        return HttpResponseRedirect("/home/")

    
# Contact Us.
def contact(request):
    if request.method == "POST":
        cname = request.POST.get("name","default")
        cmail = request.POST.get("email","default")
        cnum = request.POST.get("number","default")
        cmsg = request.POST.get("msg","default")
    contex = {}
    return render(request,'main/contactus.html',contex)


# Session Logout.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/home/")


# password change funchtion
def pwd_change(request):
    if request.method == 'POST':    
        fm = password_change(user = request.user , data= request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return HttpResponseRedirect('/home/')
    else:
        fm = password_change(user = request.user)
    contex = {'form' :fm}
    return render(request,'main/pwd_change.html',contex)
