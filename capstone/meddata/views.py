from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib import messages
from.models import Profile

# Create your views here.
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