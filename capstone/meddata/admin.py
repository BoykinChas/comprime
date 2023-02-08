from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile 


# Register your models here.
# Add Profile info with user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User 
    # Just display username files on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User 
admin.site.unregister(User)

# Rereegister User and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
