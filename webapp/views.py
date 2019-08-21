from django.shortcuts import render,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate

from django.contrib.auth.hashers import check_password

from api.models import refridgerator_display_system,history

def home(request):
    if request.user.is_authenticated:
        info = refridgerator_display_system.objects.all()
        return render(request, 'home.html',{'information':info})
    else:
        return render(request, 'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('webapp:home'))
    else:
        return render(request, 'login.html',{'err': "Error, username or password is not correct"})

def logout(request):
    auth_logout(request)
    return render(request,'login.html',{'err': "Log Out Complete!"})

def registration(request):
    if request.POST['name'] and request.POST['id']:
        refridgerator_display_system.objects.create(id=request.POST['id'],name=request.POST['name'])
        return HttpResponseRedirect(reverse('webapp:home'))
    else:
        return HttpResponseRedirect(reverse('webapp:home'))


def action(request,id):
    if request.user.is_superuser:
        try:
            if(request.POST['save']):
                print("1111111")
                thisID = refridgerator_display_system.objects.get(id=id)
                thisID.name = request.POST['name']
                print("1111111")
                print(thisID)
                thisID.save()
        except:
            if(request.POST['delete']):
                refridgerator_display_system.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('webapp:home'))
    else:
        return HttpResponseRedirect(reverse('webapp:home'))

def infor(request):
    userlog = history.objects.all()#เอามาทั้งออปเจค
    log=[]
    for data in userlog:
        m = {"datetime":data.datetime,
            "time":data.id,
            "id":data.ref_id_id,}
        log.append(m)
    return render(request,'history.html',{'log':log})


