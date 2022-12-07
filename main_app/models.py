from django.db import models

# Create your models here.

class PDFTemplate(models.Model):
    template_thumbnail = models.ImageField(upload_to="templates-thumbnails")
    template_name = models.CharField(max_length=100)
    html_file = models.FileField(upload_to="./templates")
    
    def __str__(self):
        return self.template_name