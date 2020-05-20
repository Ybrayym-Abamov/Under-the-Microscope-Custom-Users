from django.urls import path
from custom_user import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view),
    path('home/', views.main, name='homepage')
]
