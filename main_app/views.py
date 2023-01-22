from urllib import response
import django
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
import os

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from django.conf import settings

from profiles_app.models import *
from main_app.models import *
from profiles_app.forms import *

from django.contrib.auth.decorators import login_required

def landing_page(request):
    context = {}
    return render(request , "main_app/landing_page.html", context)

@login_required
def index(request):
    logged_in_user = Profile.objects.get(user = request.user)
    profile = Profile.objects.get(user=request.user)
    experiences = Experience.objects.filter(profile = profile)[::-1]
    educations = Education.objects.filter(profile = profile)[::-1]
    skills = Skills.objects.filter(profile = profile)[::-1]
    languages = Languages.objects.filter(profile = profile)[::-1]
    add_skill_form = SkillForm()   
    add_language_form = LanguagesForm() 

    # ************************************************* Start Profile form *********************************************************
    if request.method != 'POST':
        personal_info_form = ProfileForm(instance = profile )
        add_skill_form = SkillForm()
    else:
        personal_info_form = ProfileForm( request.POST, request.FILES , instance = profile )  
        if personal_info_form.is_valid():
            personal_info_form.save() 
            return redirect("main_app:index")
 # *************************************************    End Profile form *********************************************************




  # ************************************************* Start Experiences form *********************************************************
    if request.method  != 'POST':
            add_experience_form = ExperiencesForm()
    else:
        add_experience_form = ExperiencesForm(request.POST, request.FILES )
        if add_experience_form.is_valid():
            new_experience = add_experience_form.save(commit=False)
            new_experience.profile = logged_in_user
            new_experience.save()
            add_experience_form.save()
            return redirect("main_app:index")
 # ************************************************* End Experieces form *********************************************************







  # ************************************************* Start  Education form *********************************************************
    if request.method != 'POST':
        add_education_form = EducationForm()
    else:
        add_education_form = EducationForm(request.POST, request.FILES )
        if add_education_form.is_valid():
            new_education = add_education_form.save(commit=False)
            new_education.profile = logged_in_user
            new_education.save()
            add_education_form.save()
            return redirect("main_app:index")
 # ************************************************* End    Education    form *********************************************************



    context = {
        "profile":profile,
        "experiences":experiences,
        "educations":educations,
        "skills":skills,
        "languages":languages,
        "personal_info_form":personal_info_form,
        "add_skill_form":add_skill_form ,
        "add_language_form":add_language_form,
        "add_experience_form":add_experience_form,
        "add_education_form":add_education_form ,
        }
    return render(request, 'main_app/index.html', context)

@login_required  
def edit_experience(request, experience_id ):
    experience = Experience.objects.get(id = experience_id)
    if request.method != 'POST':
        experience_form = ExperiencesForm(instance=experience)
    else:
        experience_form = ExperiencesForm(instance=experience,data=request.POST)
        if experience_form.is_valid(): 
            experience_form.save()
            return redirect("main_app:index")
        
    context = {
        "experience":experience,
        "experience_form":experience_form,
        }


    return render(request, 'main_app/experience.html', context)

@login_required
def add_education(request ):
    logged_in_user = Profile.objects.get(user = request.user)
    if request.method != 'POST':
        add_education_form = EducationForm()
    else:
        add_education_form = EducationForm(request.POST, request.FILES )
        if add_education_form.is_valid():
            new_education = add_education_form.save(commit=False)
            new_education.profile = logged_in_user
            new_education.save()
            add_education_form.save()
            return redirect("main_app:index")
        
    context = {
        "add_education_form":add_education_form ,
        }
    return render(request, 'main_app/add_education.html', context)

@login_required
def add_skill(request):
    x = request.META["HTTP_REFERER"]
    print(x)
    logged_in_user = Profile.objects.get(user = request.user)
    if request.method != 'POST':
        add_skill_form = SkillForm()
    else:
        add_skill_form = SkillForm(request.POST, request.FILES )
        if add_skill_form.is_valid():
            new_skill = add_skill_form.save(commit=False)
            new_skill.profile = logged_in_user
            new_skill.save()
            add_skill_form.save()
            return redirect(x)
        

@login_required
def add_language(request):
    logged_in_user = Profile.objects.get(user = request.user)
    if request.method != 'POST':
        add_language_form = LanguagesForm()
    else:
        add_language_form = LanguagesForm(request.POST, request.FILES )
        if add_language_form.is_valid():
            new_language = add_language_form.save(commit=False)
            new_language.profile = logged_in_user
            new_language.save()
            add_language_form.save()
            return redirect("main_app:index")
        
    context = {
        "add_language_form":add_language_form ,
        }
    return render(request, 'main_app/add_education.html', context)

@login_required
def delete_experience(request, experience_id ):
    experience = Experience.objects.get(id = experience_id)
    experience.delete()
    return redirect("main_app:index")

@login_required
def edit_education(request, education_id ):
    education = Education.objects.get(id = education_id)
    if request.method != 'POST':
        education_form = EducationForm(instance=education)
    else:
        education_form = EducationForm(instance=education,data=request.POST)
        if education_form.is_valid(): 
            education_form.save()
            return redirect("main_app:index")
        
    context = {
        "education":education,
        "education_form":education_form,
        }
    return render(request, 'main_app/education.html', context)

@login_required
def delete_education(request, education_id ):
    education = Education.objects.get(id = education_id)
    education.delete()
    return redirect("main_app:index")

@login_required
def delete_skill(request, skill_id ):
    skill = Skills.objects.get(id = skill_id)
    skill.delete()
    return redirect("main_app:index")

@login_required
def delete_language(request, language_id ):
    languages = Languages.objects.get(id = language_id)
    languages.delete()
    return redirect("main_app:index")

@login_required
def templates_list(request):
    templates = PDFTemplate.objects.all()[::-1]
    profile = Profile.objects.get(user=request.user)
    context = {
        "templates":templates,
        "profile":profile,
    }
    return render(request, 'main_app/template_list.html', context)


def link_callback(uri, rel):
	"""
	Convert HTML URIs to absolute system paths so xhtml2pdf can access those
	resources
	"""
	result = finders.find(uri)
	if result:
			if not isinstance(result, (list, tuple)):
					result = [result]
			result = list(os.path.realpath(path) for path in result)
			path=result[0]
	else:
			sUrl = settings.STATIC_URL        # Typically /static/
			sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
			mUrl = settings.MEDIA_URL         # Typically /media/
			mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

			if uri.startswith(mUrl):
					path = os.path.join(mRoot, uri.replace(mUrl, ""))
			elif uri.startswith(sUrl):
					path = os.path.join(sRoot, uri.replace(sUrl, ""))
			else:
					return uri

	# make sure that file exists
	if not os.path.isfile(path):
			raise Exception(
					'media URI must start with %s or %s' % (sUrl, mUrl)
			)
	return path


def render_pdf_view(request , profile_id , template_id ):
    profile = Profile.objects.get(id = profile_id)
    choosen_template = PDFTemplate.objects.get(id=template_id)
    print(choosen_template.html_file.name)
    name = profile.first_name + " " + profile.last_name
    full_name = name+".pdf"
    print(full_name)
    experiences = Experience.objects.filter(profile = profile)
    educations = Education.objects.filter(profile = profile)
    skills = Skills.objects.filter(profile = profile)
    languages = Languages.objects.filter(profile = profile)
    
    #template_path = 'main_app/pdf_template.html'
    template_path = f'{choosen_template.html_file.name}'
    context = {
        "profile":profile,
        "experiences":experiences,
        "educations" : educations,
        "skills":skills,
        "languages":languages, 
        
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = f'attachment; filename={full_name}'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_test(request , profile_id ):
    profile = Profile.objects.get(id = profile_id)
  
    name = profile.first_name + " " + profile.last_name
    full_name = name+".pdf"

    experiences = Experience.objects.filter(profile = profile)
    educations = Education.objects.filter(profile = profile)
    skills = Skills.objects.filter(profile = profile)
    languages = Languages.objects.filter(profile = profile)
    
    template_path = 'main_app/pdf_template.html'

    context = {
        "profile":profile,
        "experiences":experiences,
        "educations" : educations,
        "skills":skills,
        "languages":languages, 
        
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
   # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = f'attachment; filename={full_name}'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


