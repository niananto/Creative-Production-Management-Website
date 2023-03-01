from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse
from estimation.models import *


class CSOLoginView(CreateView):
  def get(self, request):
    return render(request, 'estimation/login.html')

  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']

    cso = None

    try:
      cso = CSO.objects.get(username=username, password=password)  
    except:
      return render(request, 'estimation/login.html')

    # url = reverse()
    return redirect('create-estimation/' + str(cso.username) + '/')

def create_estimation(request, username:str):
  return render(request, 'estimation/estimation.html', {'username': username})
