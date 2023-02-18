from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('doctor', views.doctor, name='doctor'),
    path('add_milestone', views.add_milestone, name='add_milestone'),
    path('milsestone', views.milestone, name='milestone'),
]

