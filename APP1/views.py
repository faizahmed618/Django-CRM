from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm #Not using this
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms

class Signupview(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = forms.Customusercreationform
    def get_success_url(self):
        return reverse("login")

class Landingpageview(generic.TemplateView):
    template_name = "landing.html"

class Land(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "landing.html")
    
def landing(request):
    return render(request, "landing.html")

def login(request):
    return render(request, "APP1/login.html")

class Leadlistview(LoginRequiredMixin, generic.ListView):
    template_name = "APP1/leads.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

def leads(request):
    leads = models.Lead.objects.all()
    data = { "leads": leads}
    return render(request, "APP1/leads.html", context = data)

class Leaddetailview(LoginRequiredMixin, generic.DetailView):
    template_name = "APP1/leads_details.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

def leads_detail(request, key):
    leads = models.Lead.objects.get(id=key)
    data = { "leads": leads,
             "test": key}
    return render(request, "APP1/leads_details.html", context = data)

class Leadcreateview(LoginRequiredMixin, generic.CreateView):
    template_name = "APP1/create_form.html"
    form_class = forms.create_form_model
    def get_success_url(self):
        return reverse("APP1NameSpace:leads")
    
    def form_valid(self, form):
        send_mail(subject="A Lead has been created",
                  message="GO TO site to check the lead",
                  from_email="test@test.com",
                  recipient_list=["test2@test.com"])
        return super(Leadcreateview,self).form_valid(form)

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

class Leadupdateview(LoginRequiredMixin, generic.UpdateView):
    queryset = models.Lead.objects.all()
    form_class = forms.create_form_model
    template_name = "APP1/update_form.html"
    def get_success_url(self):
        return reverse("APP1NameSpace:leads")
        # return redirect("/APP1/leads") this doesnt work in class

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

# below function is same as above about updating

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

class Leaddeleteview(LoginRequiredMixin, generic.DeleteView):
    template_name = "APP1/delete_form.html"
    queryset = models.Lead.objects.all()
    def get_success_url(self):
        return reverse("APP1NameSpace:leads")

def delete_lead(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/APP1/leads")