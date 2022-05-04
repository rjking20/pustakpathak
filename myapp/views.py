from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Imgstore
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required,permission_required
from datetime import datetime

@login_required(login_url='/signin')
def hindhome(request):
    books = Imgstore.objects.all()
    time = datetime.now()
    greet = ''
    hour = int(time.strftime('%H'))


    if hour < 12:
        greet = 'सुप्रभात'
    elif hour < 17:
        greet = 'शुभ दिन'
    else:
        greet = 'शुभ संध्या'
    
    
    context={
        'books':books,
        'greet':greet
    }

    return render(request,'home.html',context=context)
 
@login_required(login_url='/signin')
def enghome(request):
    books = Imgstore.objects.all()
    time = datetime.now()
    greet = ''
    hour = int(time.strftime('%H'))


    if hour < 12:
        greet = 'Good Morning'
    elif hour < 17:
        greet = 'Good Afternoon'
    else:
        greet = 'Good Evening'
    
    context={
        'books':books,
        'greet':greet
    }

    return render(request,'index.html',context=context)
  
def signin(request):
    return render(request,'login.html')


def signup(request):
    if not get_referer(request):
        return redirect('/error')
    return render(request,'register.html')
    
# ------------------ Register ------------------

def register(request):
    if not get_referer(request):
        return redirect('/error')
        
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        passw=request.POST['pass']
        rpassw=request.POST['rpass']
        email = request.POST['email']

        if passw == rpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is exists')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=uname,password=passw,first_name=fname,last_name=lname)
                user.save()
                return redirect('/signin')
    else:
        return render(request,'register.html')    


# ------------------- Login ----------------------

def login(request):
    if not get_referer(request):
        return redirect('/error')
        
    if request.method == 'POST':

        uname = request.POST['uname']
        passw = request.POST['pass']
        
        user = auth.authenticate(username=uname,password=passw)

        if user is not None:
            auth.login(request,user)
            request.session['user']=uname
            request.session.set_expiry(1800)
            return redirect('/en')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/signin')
    
    return redirect('/signin')


# ---------------- Logout -----------------

def logout(request):
    global lan
    if not get_referer(request):
        return redirect('/error')
    auth.logout(request)
    try:
        request.session.clear_expired()
        del request.session['user']
    except:
        pass
    return redirect('/en')


def error(request):
    return render(request,'error.html')

def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer
