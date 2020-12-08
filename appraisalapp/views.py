
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
from .models import Company
from django.db.models import Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateCompanyForm

# Create your views here.
def landing(request):
    
    return render(request,"landing.html")

def logout(request):
    
    return render(request,"logout.html")    

def createcompany(request):
    if request.method == "POST":
        create = CreateCompanyForm(request.POST, instance = request.user)
        if create.is_valid():
            create.save()
            return redirect('companylist')
    else:
        create = CreateCompanyForm(instance=request.user)  

    params = {
        'create':create
    }          
    return render(request, 'companies/company_form.html', params)


def companylist(request):
    companies = Company.objects.all().order_by('-date_posted')
    return render(request, 'companies/company_home.html',{'companies':companies})

def companydetails(request, pk):

    company = get_object_or_404(Company, pk = pk)

    params = {
        'company': company,
    }

    return render(request, 'companies/company_details.html', params)




