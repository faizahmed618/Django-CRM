from django.urls import path
from . import views

app_name = 'Agent'

urlpatterns = [
    path("agents-list/", views.Agentlistview.as_view(), name="agent-list"),
    path("agents-create/", views.Agentcreateview.as_view(), name="agent-create"),
    path("check/", views.check),
]