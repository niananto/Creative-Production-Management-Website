from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
# from models import *
class CSOLoginView(LoginView):
  template_name = 'estimation/login.html'

def estimation(request):
  # contex = ['anup', 'showvik']
  return render(request, 'estimation/estimation.html')

