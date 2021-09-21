from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views
from django.views.generic import TemplateView

from .views import SignUpView

urlpatterns = [
    path('', views.LoginView.as_view(template_name='authy/login.html'), name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('signup/', SignUpView, name='signup'),
]
