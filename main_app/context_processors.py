from profiles_app.models import *
from main_app.models import *

def data(request):
       try:
              print("Context processor no eror")
              profile = Profile.objects.get(user=request.user)

              return {
              "profile":profile
              }
              
       except:
              profile = ""
              return {"profile":profile}
