from django import forms
from django.forms import ModelForm
from .models import Doctor, Milestone


class MilestoneForm(ModelForm):
    class Meta:
        model = Milestone
        fields = ('calms', 'looks', 'happy', 'smiles', 'sounds', 'loud', 'watches', 'toy', 'head', 'move', 'hands',)
        
        # widgets = {
        #     'calms': forms.Select(attrs={'class':'form-control'}),
        #     'looks': forms.Select(attrs={'class':'form-control'}),
        #     'happy': forms.Select(attrs={'class':'form-control'}),
        #     'smiles': forms.Select(attrs={'class':'form-control'}),
        #     'sounds': forms.Select(attrs={'class':'form-control'}),
        #     'loud': forms.Select(attrs={'class':'form-control'}), 
        #     'watches': forms.Select(attrs={'class':'form-control'}),
        #     'toy': forms.Select(attrs={'class':'form-control'}), 
        #     'head': forms.Select(attrs={'class':'form-control'}), 
        #     'move': forms.Select(attrs={'class':'form-control'}),
        #     'hands': forms.Select(attrs={'class':'form-control'}),
		# }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'clinic', 'address', 'zip_code', 'phone', 'specialty',)
      
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Doctors Name'}),
			'clinic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Clinic/Hospital'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'specialty': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Specailty'}),
		}
        
