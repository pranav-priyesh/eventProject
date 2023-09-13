from django import forms
from .models import Applicant

class Applicantform(forms.ModelForm):
    class Meta:
        model=Applicant
        fields=['full_name','email','phone']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'align','placeholder': 'Enter your full name' }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'align','placeholder': 'Enter your Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'align','placeholder': 'Enter your Phone'}))