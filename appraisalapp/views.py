
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
# from .models import Project,Profile,Rating
from django.db.models import Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
# from .forms import UpdateUserForm,UpdateUserProfileForm,NewPostForm,ProjectRatingForm

# Create your views here.
def landing(request):
    
    return render(request,"landing.html")

def logout(request):
    
    return render(request,"logout.html")    
