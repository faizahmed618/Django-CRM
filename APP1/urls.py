from django.urls import path
from . import views

app_name = 'APP1'

urlpatterns = [
    path("login/", views.login, name = "login"),
    # path("leads/", views.leads, name = "leads"),
    path("leads/", views.Leadlistview.as_view(), name = "leads"),
    # path("leads_details/<int:key>/", views.leads_detail, name = "lead_details"),
    path("leads_details/<int:pk>/", views.Leaddetailview.as_view(), name = "lead_details"),
    # path("leads_details/<int:pk>/update/", views.update_lead, name = "update_lead"),
    path("leads_details/<int:pk>/update/", views.Leadupdateview.as_view(), name = "update_lead"),
    # path("leads_details/<int:pk>/delete/", views.delete_lead, name = "delete_lead"),
    path("leads_details/<int:pk>/delete/", views.Leaddeleteview.as_view(), name = "delete_lead"),
    # path("create_lead/", views.new_lead, name = "new_lead")
    path("create_lead/", views.Leadcreateview.as_view(), name = "new_lead")
]