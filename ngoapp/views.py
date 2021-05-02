from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tinfo, Sinfo , Announcement
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout, models
from datetime import date

def index(request):
    return render(request,'index.html')

def register(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if Tinfo.objects.filter(Email = email).exists() or Sinfo.objects.filter(Email = email).exists():
            err = 'Email already taken. Try a different one.'
            
        else:
            obj1 = User.objects.create(
                username = email,
                email = email,
            )

            obj1.set_password(request.POST.get('passw'))
            obj1.save()

            name = request.POST.get('name')
            num = request.POST.get('num')
            add = request.POST.get('add')
            passw = request.POST.get('passw')
            cpassw = request.POST.get('cpassw')

            obj2 = Tinfo.objects.create(
                Email = email,
                Name = name ,
                Password = passw,
                PhoneNo = num,
                Address = add
            )
            obj2.save()
            return redirect("teacherlogin")
        
    template_name = 'register.html'
    context={'err':err}
    return render(request, template_name,context)


def studreg(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if Tinfo.objects.filter(Email = email).exists() or Sinfo.objects.filter(Email = email).exists():
            err = 'Email already taken. Try a different one.'
            
        else:
            obj1 = User.objects.create(
                username = email,
                email = email,
            )

            obj1.set_password(request.POST.get('passw'))
            obj1.save()

            name = request.POST.get('name')
            num = request.POST.get('num')
            std = request.POST.get('std')
            passw = request.POST.get('passw')
            cpassw = request.POST.get('cpassw')

            obj2 = Sinfo.objects.create(
                Email = email,
                Name = name ,
                Password = passw,
                ParNo = num,
                Std = std
            )
            obj2.save()
            return redirect("stud_dash")
        
    template_name = 'studreg.html'
    context={'err':err}
    return render(request, template_name,context)

def teacherlogin(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passw')
        user = authenticate(request, username = email, password = password)
        if user is not None and Tinfo.objects.filter(Email = email).exists():
            auth.login(request, user)
            return redirect('teacher_dash')
        else:
           err = 'Input correct email and password'
    
    template_name = 'teacherlogin.html'
    context={'err':err}
    return render(request, template_name,context)

def studlogin(request):
    err=""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passw')
        user = authenticate(request, username = email, password = password)
        if user is not None and Sinfo.objects.filter(Email = email).exists():
            auth.login(request, user)
            return redirect('stud_dash')
        else:
           err = 'Input correct email and password'
    
    template_name = 'studlogin.html'
    context={'err':err}
    return render(request, template_name,context)

def logout(request):
    models.auth.logout(request)
    return redirect('/')

def teacher_dash(request):
    return render(request,'teacher_dash.html')

def testdash(request):
    return render(request,'testdash.html')

def newtest(request):
    return render(request,'newtest.html')

def createtest(request):
    return render(request,'createtest.html')

def announ(request):
    return render(request,'announ.html')

def createannoun(request):
    return render(request,'createannoun.html')

def stud_dash(request):
    return render(request,'stud_dash.html')

def viewannoun(request):
    
    toda = date.today()
    an = Announcement.objects.all()
    ar=[]
    for i in an:
    
        if i.expires_on>toda:
            ar.append(i)
            
    print(str(len(ar))+"\n")
    return render(request, 'viewannoun.html', {'ann':ar})
    

def pendtest(request):
    return render(request,'pendtest.html')

def test(request):
    return render(request,'test.html')

def pre(request):
    return render(request,'pre.html')

def post(request):
    return render(request,'post.html')

def feed(request):
    return render(request,'feed.html')

def addresc(request):
    return render(request,'addresc.html')

def viewresc(request):
    return render(request,'viewresc.html')

def postannou(request):
     if request.method == 'POST':
          heading = request.POST.get('heading')
          body=request.POST.get('body')
          date=request.POST.get('date')
          obj2 = Announcement.objects.create(
                heading=heading,
                body=body,
                expires_on=date
            )
          obj2.save()
     return redirect("createannoun")