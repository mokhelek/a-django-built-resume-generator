from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from main_app.models import *
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.
def compress(image):
    im =Image.open(image)
    im_io = BytesIO()
    im.save(im_io,'PNG',quality=80)
    new_image = File(im_io,name=image.name)
    return new_image


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default=1 ) # this has the username inside
    avatar = models.ImageField(null=True, upload_to="avatars", blank=True , default='default.png')
    first_name = models.CharField(max_length=200,null=True, blank=True)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    job_title = models.CharField(max_length=200,null=True, blank=True)
    bio = models.TextField( null=True, blank=True)
    email = models.EmailField()
    cell = models.CharField(max_length=15,null=True, blank=True )
    
    
 
    location = models.CharField(max_length=300, null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    personal_link = models.URLField(null=True, blank=True)
 
    
    def __str__(self):
        return self.last_name + "  " + self.first_name
    

class Skills(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE )
    skill_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.skill_name

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    job_description = models.TextField()
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    

    
    def __str__(self):
        return self.job_title

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE )
    institution_name = models.CharField(max_length=200)
    qualification_name = models.CharField(max_length=200)
    education_description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    

class Projects(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE )
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    project_thumbnail = models.ImageField(null=True, upload_to="projects", blank=True)
    project_url = models.URLField()
    
    def save(self,*args,**kwargs):
        new_image = compress(self.project_thumbnail)
        self.project_thumbnail = new_image
        super().save(*args,**kwargs)

class Languages(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE )
    language_name = models.CharField(max_length=200)
 
 
