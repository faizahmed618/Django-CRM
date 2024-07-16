from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from APP1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.landing, name="Landing"),
    path("", views.Landingpageview.as_view(), name="Landing"),
    path("APP1/", include("APP1.urls", namespace ="APP1NameSpace")),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("signup/", views.Signupview.as_view(), name='signup')
]

if settings.DEBUG:
    # urlpatterns += (static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))

