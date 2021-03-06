from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User      

class SignUpForm(UserCreationForm): 

    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(help_text='Email')
    about = forms.CharField(max_length=150, help_text='About')
    dob = forms.DateTimeField(label="Date", required=True, widget=forms.NumberInput(attrs={'type':'date'}))
    address = forms.CharField(max_length=150, help_text='Address')
    user_img = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2','dob','email','about','address','user_img')
 
