from django.urls import path
from . import views 
from . views import Notes

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('doctor', views.doctor, name='doctor'),
    path('add_milestone', views.add_milestone, name='add_milestone'),
    path('milestone', views.milestone, name='milestone'),
#     path('add_notes', views.add_notes, name='add_notes'),
    path('notes', Notes.as_view(), name='notes'),
]

