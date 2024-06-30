from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name = "login"),
    path("leads/", views.leads, name = "leads"),
    path("leads_details/<int:pk>", views.leads_detail, name = "lead_details"),
    path("leads_details/<int:pk>/update", views.update_lead, name = "lead_details"),
    path("create_lead", views.new_lead, name = "new_lead")
]