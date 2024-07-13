from django.contrib import admin
from django.urls import path, include
from APP1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.landing, name="Landing"),
    path("APP1/", include("APP1.urls", namespace ="APP1NameSpace"))
]
