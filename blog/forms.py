from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Post
from django import forms
from .models import Ticket
class signupForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'})}
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TimeInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 
class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','des']
        labels={'title':'Title','des':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'des':forms.Textarea(attrs={'class':'form-control'})}

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['visitor_name', 'checkin', 'image']