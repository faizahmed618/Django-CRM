from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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
    form1 = forms.create_form_model()
    if request.method == "POST":
        form1 = forms.create_form_model(request.POST)
        if form1.is_valid():
            form1.save()
            # webpage = reverse("leads")
            # return HttpResponseRedirect(webpage) this can also be used but preffered when sending data
            return redirect("/APP1/leads")
    data = {"form": form1}
    return render(request, "APP1/create_form.html", context = data)

# the below function is same but using normal form.
# def new_lead(request):
#     form = forms.create_form()
#     if request.method == "POST":
#         form = forms.create_form(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             firstName = form.cleaned_data["firstName"]
#             lastName = form.cleaned_data["lastName"]
#             age = form.cleaned_data["age"]
#             agent = models.Agent.objects.get(id=1)
#             models.Lead.objects.create(firstName = firstName,
#                                        lastName = lastName,
#                                        age = age,
#                                        agent = agent)
#             # webpage = reverse("leads")
#             # return HttpResponseRedirect(webpage)
#             return redirect("/APP1/leads")
#     data = {"form": form}
#     return render(request, "APP1/create_form.html", context = data)

def update_lead(request, pk):
    lead = models.Lead.objects.get(id=pk)
    form = forms.create_form_model(instance=lead)
    if request.method == "POST":
        form = forms.create_form_model(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/APP1/leads")
    data = {"form": form,
            "lead": lead}
    return render(request, "APP1/update_form.html", context = data)

# def update_lead(request, pk):
#     lead = models.Lead.objects.get(id=pk)
#     form = forms.create_form()
#     if request.method == "POST":
#         form = forms.create_form(request.POST)
#         if form.is_valid():
#             lead.firstName = form.cleaned_data["firstName"]
#             lead.lastName = form.cleaned_data["lastName"]
#             lead.age = form.cleaned_data["age"]
#             lead.agent = lead.agent
#             lead.save()
#             return redirect("/APP1/leads")
#     data = {"form": form,
#             "lead": lead}
#     return render(request, "APP1/update_form.html", context = data)
        