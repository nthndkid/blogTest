from django.urls import path
from . import views

urlpatterns = [
    # path('', views.landing_view, name='landing_view'),
    path('', views.home, name='home'),
    # path('login_user', views.login_user, name='login_user'),
    # path('logout_user', views.logout_user, name='logout_user'),
    # path('register', views.register_user, name='register_user'),
]    