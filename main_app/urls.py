from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('',views.landing_page , name = "landing_page"),
	path('profile/', views.index , name = 'index'),
    path("pdf_view/<int:profile_id>/<int:template_id>/",views.render_pdf_view , name = "pdf_view" ),
    path("pdf_view/<int:profile_id>/",views.render_pdf_view_test , name = "pdf_view_test" ),
    
    # forms
    path("experiences/<int:experience_id>/", views.edit_experience , name="experiences"),
    path("education/<int:education_id>/", views.edit_education , name="education"),
    
    # deleting
    path("delete-experience/<int:experience_id>/", views.delete_experience, name="delete_experience"),
    path("delete-education/<int:education_id>/", views.delete_education, name="delete_education"),
    path("delete-skill/<int:skill_id>/", views.delete_skill, name="delete_skill"),
    path("delete-languages/<int:language_id>/", views.delete_language, name="delete_language"),
    
    # adding
    path("add-experience/",views.add_experience, name = "add_experience"),
    path("add-education/",views.add_education, name = "add_education"),
    path("add-skills/",views.add_skill, name = "add_skill"),
    path("add-languages/",views.add_language, name = "add_language"),
    path("templates-list/",views.templates_list, name = "templates_list"),
    

    
]


