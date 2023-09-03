from django.shortcuts import render,redirect
from main.forms import RegisterForm,UserChange
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login as user_login,logout as user_logout,update_session_auth_hash
from datetime import datetime,timedelta
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created Succssfully")
            messages.warning(request,"warning")
            messages.info(request,"info")
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form =RegisterForm()
    return render(request,"signup.html",{'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=name,password=password)
            if user is not None:
                user_login(request,user)
                return redirect('profile')
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form =UserChange(request.POST,instance = request.user)
        if form.is_valid():
            messages.success(request,"User updated successfuly")
            messages.warning(request,"warning")
            messages.info(request,"info")
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form =UserChange(instance = request.user)
    return render(request,"profile.html",{'form':form})

def logout(request):
    user_logout(request)
    return redirect('login')

def pass_change(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user = request.user)
    
    return render(request,"passchange.html",{'form':form})
    
def pass_change2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    
    else:
        form = SetPasswordForm(user = request.user)
    
    return render(request,"passchange.html",{'form':form})

def change_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form =UserChange(request.POST,instance = request.user)
        if form.is_valid():
            messages.success(request,"User updated successfuly")
            messages.warning(request,"warning")
            messages.info(request,"info")
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form =UserChange()
    return render(request,"profile.html",{'form':form})

def cookie_demo(request):
    response = render(request,"cookie.html")
    response.set_cookie('name','rahim',max_age=3600,expires=datetime.utcnow()+timedelta(days=7))
    return response
def get_cookie(request):
    
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'cookie.html',{'name':name})


def delete_cookie(request):
    response = render(request,"cookie.html")
    response.delete_cookie('name')
    return response

def set_session(request):

    data = {
        'name':'rahim',
        'age':23,
        'language':'bangla'
    }
    # get session expiration age
    session_age = request.session.get_session_cookie_age()
    #get session expiray data
    expiray_date = request.session.get_session_cookie_age()
    
    request.session.update(data)
    return render(request,'cookie.html')

def get_session(request):
    if 'name' in request.session:

        name= request.session.get('name')
        age= request.session.get('age')
        language= request.session.get('language')
        data = {'name':name,'age':age,'language':language}
        # update the session expiry age
        request.session.modified = True
        return render(request,'cookie.html',{'data':data})
    else:
        return HttpResponse("Your Session has been expired")


def delete_session(request):
     # for deleting particular data
    del request.session['name']
    #  for deleting all data
    request.session.flush()
    request.session.clear_expired() #
    return render(request,'cookie.html')