
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
from .models import Company,Review
from django.db.models import Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateCompanyForm,CreateReviewForm

# Create your views here.
def landing(request):
    
    return render(request,"landing.html")

def logout(request):
    
    return render(request,"logout.html")    

def createcompany(request):
    current_user = request.user
    if request.method == "POST":
        create = CreateCompanyForm(request.POST, request.FILES)
        if create.is_valid():
            new_company = create.save(commit=False)
            new_company.user = current_user

            new_company.save()
            return redirect('companylist')
    else:
        create = CreateCompanyForm()  

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

@login_required(login_url='/accounts/login/')
def addreview(request, id):
    current_user = request.user

    current_company = Company.objects.get(id=id)
    if request.method == "POST":
        review = CreateReviewForm(request.POST, instance = request.user)
        if review.is_valid():
            new_review = review.save(commit=False)
            new_review.user = current_user
            new_review.company = current_company
            new_review.save()
            return redirect('reviewhome', id)
    else:
        review = CreateReviewForm(instance=request.user)  

    params = {
        'review':review
    }          
    return render(request, 'reviews/review_form.html', params)

def reviewhome(request):
    reviews = Review.objects.all().order_by('-date_posted')
    return render(request, 'reviews/review_home.html',{'reviews':reviews})

@login_required(login_url='/accounts/login/')
def reviewdetails(request, pk):   
    review = get_object_or_404(Review, pk = pk)

    params = {
        'review': review,
    }

    return render(request, 'reviews/review_details.html', params)
