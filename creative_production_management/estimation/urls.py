from django.urls import path
from . import views

urlpatterns = [
  path('', views.CSOLoginView.as_view(), name='login'),
  path('create-estimation/<str:username>/', views.create_estimation, name='create-estimation'),
]