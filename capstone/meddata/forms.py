from django import forms
from django.forms import ModelForm
from .models import Doctor


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'address', 'zip_code', 'phone', 'specialty')
        labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'specialty': '',		
		}
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Doctors Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'specialty': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Specailty'}),
		}