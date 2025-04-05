from django.urls import path
from .views import signup_view, login_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    #path('login/', login_view, name='login'),
    #path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

