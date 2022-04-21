from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Cbc,ConfirmDoctor
from .models import Comments
from django.contrib.auth.hashers import make_password

from home import models

# you have to pass string as parameter
password = "123"
make_password(password)
from django.core.validators import RegexValidator
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    username= forms.CharField(label='Usename', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),help_text='Enter Username in any format')
    first_name= forms.CharField(label='First_name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Firstname'}),help_text='Enter Firstname in alphabets only')
    last_name= forms.CharField(label='Last_name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Lastname'}),help_text='Enter lastname in alphabets only')
    email= forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'username@gmail.com'}),help_text='Enter Email in username@gmail.com')
    height= forms.IntegerField(label='Height', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Height in cms'}),help_text='Enter height in Numbers only')
    weight= forms.IntegerField(label='Weight', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Weight in Kg'}),help_text='Enter Weight in Numbers only')
    # dob= forms.DateField(label='Date', 
    #                 widget=forms.TextInput(attrs={'placeholder': 'Enter your dob'}))
    
    

    class Meta:
        model = User
        fields = ("username","first_name",'last_name', "email", "password1", "password2","height","weight","gender")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ConfirmDoctor(forms.ModelForm):
    class Meta:
        model = ConfirmDoctor
        fields = ('username','password')


from .models import Doctor
class DoctorForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username= forms.CharField(label='First_Name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your firstname'}),help_text='Enter Your Name in Alphabets only', error_messages = {
                 'required':"Please Enter your Name"})
    Surname= forms.CharField(label='Surname', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Surname'}),help_text='Enter Surname in alphabets only')
    email= forms.CharField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Email-id'}),help_text='Enter email in username@gmail.com form only')
    phone_number= forms.CharField(label='phonenumber', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Correct Phone Number'}),help_text='Enter 10 digit number only')
    
   
    
    
    # password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Doctor
        fields = ('username','Surname', 'email','gender','phone_number','Specialization')
    def save(self, commit=True):
        user = super(DoctorForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UploadForm(forms.ModelForm):
    class Meta:
        model = Cbc
        fields = ('name', 'file')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("field_name",)

class ConfirmForm(forms.ModelForm):
    
    class Meta:
        model = Cbc
        fields = ("rbc","wbc","pc","hgb","rcd","mchc","mpv","pcv","mcv","name")
        
class EditProfileDoctor(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    username= forms.CharField(label='Usename', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),help_text='Enter Username in any format')
    Surname= forms.CharField(label='Surname', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Firstname'}),help_text='Enter Firstname in alphabets only')
    email= forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'username@gmail.com'}),help_text='Enter Email in username@gmail.com')
    phone_number= forms.IntegerField(label='PhoneNumber', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Phone Number 9874651230'}),help_text='Enter 10 Digits Phonenumber only')
    
    class Meta:
        model = Doctor
        fields = ('username','Surname', 'email','gender','phone_number','Specialization')
class EditProfile(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    username= forms.CharField(label='Usename', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),help_text='Enter Username in any format')
    first_name= forms.CharField(label='First_name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Firstname'}),help_text='Enter Firstname in alphabets only')
    last_name= forms.CharField(label='Last_name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Lastname'}),help_text='Enter lastname in alphabets only')
    email= forms.EmailField(label='Email', 
                    widget=forms.TextInput(attrs={'placeholder': 'username@gmail.com'}),help_text='Enter Email in username@gmail.com')
    height= forms.IntegerField(label='Height', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Height in cms'}),help_text='Enter height in Numbers only')
    weight= forms.IntegerField(label='Weight', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your Weight in Kg'}),help_text='Enter Weight in Numbers only')
    class Meta:
        model = User
        fields = ("username","first_name",'last_name', "email", "height","weight","gender")