from django.shortcuts import redirect, render
from django.urls import reverse
from . models import job
from django.core.paginator import Paginator
from . forms import Applyform , jobform

# Create your views here.
def job_list(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list,3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj}
    return render(request,'job/job_list.html',context)


def job_details(request ,slug ):
    job_details = job.objects.get(slug=slug)
    
    if request.method == "POST":
        forms = Applyform(request.POST , request.FILES)
        if forms.is_valid():
            myform = forms.save(commit=False)
            myform.job =job_details
            myform.save()
            

    else:
        forms = Applyform()
    context = {'job': job_details , 'forms':forms }
    return render (request , 'job/job_details.html',context)


def add_job (request):
    if request.method == "POST":
        forms = jobform(request.POST , request.FILES)
        if forms.is_valid():
            myform = forms.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list')) 
        

    else:
        forms = jobform()


    return render (request ,'job/add_job.html',{'forms':forms}) 
