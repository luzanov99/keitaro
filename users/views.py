from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, DateFilterForm
from rest_framework import viewsets, status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from users.request import keitaro

class CreateUser(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User(username=serializer.data['username'])
            user.set_password(serializer.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('http://keratis.herokuapp.com/users/dashboard/')
                    #return render(request, 'users/dashboard.html', {'section':'dashboard'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/users/login/')
def dashboard(request):
    
    if request.method == 'POST':
        
        form = DateFilterForm(request.POST)
        print(form.data)
        start_date = form.data["start_date_year"]+'-'+form.data["start_date_month"]+'-'+form.data["start_date_day"]
        end_date = form.data["end_date_year"]+'-'+form.data["end_date_month"]+'-'+form.data["end_date_day"]
        result = keitaro(kl_id=form.data["data_name"], start_date=start_date, end_date=end_date)
        return render(request, 'users/dashboard.html', {'bayers':result, 'form': form})
       
    else:
        form = DateFilterForm(request.POST)
        result = keitaro()
        return render(request, 'users/dashboard.html', {'bayers':result, 'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('http://keratis.herokuapp.com/users/login/')