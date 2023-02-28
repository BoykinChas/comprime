from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Profile, Doctor, Milestone, Notes
from .forms import DoctorForm, MilestoneForm
from django.http import HttpResponseRedirect

# Create your views here.
def add_milestone(request):
    submitted = False
    if request.method == "POST":
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_milestone?submitted=True')
    else:
        form = MilestoneForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render (request, 'add_milestone.html', {"form":form, 'submitted':submitted})

def milestone(request):
    if request.user.is_authenticated:
        milestone_list = Milestone.objects.filter(user=request.user)
    return render(request, 'milestone.html', {'milestone_list': milestone_list})

def doctor(request):
    if request.user.is_authenticated:
        doctor_list = Doctor.objects.filter(user=request.user)
    return render(request, 'doctor.html', {'doctor_list': doctor_list})


def add_doctor(request):
    submitted = False
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_doctor?submitted=True')
    else:
        form = DoctorForm
        if 'submitted' in request.GET:
            submitted = True

    return render (request, 'add_doctor.html', {"form":form, 'submitted':submitted})

class Notes(ListView):
    model = Notes
    template_name = 'notes.html'

class ProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.'

def home(request):
    return render(request, 'home.html')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, "profile.html", {"profile": profile})
    else:
        messages.success(request, ("You Must be Loggied In To View This Page"))
        return redirect('home')