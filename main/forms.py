from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from . models import Contactus

class Registration(UserCreationForm):
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control text-info","placeholder":"Password"}))
    password2 = forms.CharField( label = "Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control text-info","placeholder":"Confirm Password"}))
    class Meta :
        model = User
        fields = ["username","first_name","last_name","email"]
        widgets ={"username":forms.TextInput(attrs={"class":"form-control text-info","placeholder":"Username"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control text-info","placeholder":"First name"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control text-info","placeholder":"Last name"}),
                 "email":forms.EmailInput(attrs={"class":"form-control text-info","placeholder":"Email"}),
        }

class User_login(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control text-info","placeholder":"Password"}))
    username = forms.CharField(widget=forms.TextInput({"class":"form-control text-info","placeholder":"Username"}))

class password_change(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput({"class":"form-control text-info","placeholder":"Old Password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput({"class":"form-control text-info","placeholder":"New Password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput({"class":"form-control text-info","placeholder":"New Password"}))
   
# class Contact(forms.ModelForm):
#     class Meta:
#         model = Contactus
#         feilds = '__all__'