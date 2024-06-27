from django.shortcuts import render
from django.http import HttpResponse
from . import models, forms

# Create your views here.
def login(request):
    return render(request, "APP1/login.html")

def leads(request):
    leads = models.Lead.objects.all()
    data = { "leads": leads}
    return render(request, "APP1/leads.html", context = data)

def leads_detail(request, pk):
    leads = models.Lead.objects.get(id=pk)
    data = { "leads": leads}
    return render(request, "APP1/leads_details.html", context = data)

def new_lead(request):
    form = forms.create_form()
    data = { "form": form}
    return render(request, "APP1/create_form.html", context = data)