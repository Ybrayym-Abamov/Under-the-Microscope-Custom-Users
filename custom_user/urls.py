from django.urls import path
from custom_user import views

urlpatterns = [
    path('signup/', views.signup_view),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view),
    path('', views.main, name='homepage')
]
