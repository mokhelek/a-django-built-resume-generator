from dataclasses import fields
from logging import PlaceHolder
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="Required")
    username = forms.CharField(widget=forms.TextInput , help_text = '')
    password1 = forms.CharField(widget=forms.TextInput , help_text = '')
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")
        
        
class ProfileForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea , label='Summery')
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
  
  
class ExperiencesForm(ModelForm):
    start_date = forms.DateField(widget = forms.widgets.DateInput(attrs={'type':'date','rows':1 ,'columns':2}))
    end_date = forms.DateField(widget = forms.widgets.DateInput(attrs={'type':'date','rows':1 ,'columns':2}))

    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['profile']
        
class EducationForm(ModelForm):
    start_date = forms.DateField(widget = forms.widgets.DateInput(attrs={'type':'date','rows':1 ,'columns':2}))
    end_date = forms.DateField(widget = forms.widgets.DateInput(attrs={'type':'date','rows':1 ,'columns':2}))
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['profile']
        
class SkillForm(ModelForm):
    skill_name = forms.CharField(widget=forms.TextInput , label='', help_text= "add skill" )        

    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['profile']
        
        
class LanguagesForm(ModelForm):
    language_name = forms.CharField(widget=forms.TextInput , label='', help_text= "add skill" )        

    class Meta:
        model = Languages
        fields = '__all__'
        exclude = ['profile']
        
    