from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from custom_user.models import MyUser
from custom_user.forms import LoginForm, SignUpForm
from adastra.settings import AUTH_USER_MODEL


# REFERENCES:
# https://docs.djangoproject.com/en/3.0/topics/auth/default/
# https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m


@login_required  # to view the main page, visitors must be logged in
def main(request):
    # retrieving all of the data from the model I created
    data = MyUser.objects.all()
    # and rendering all of it in the main page
    return render(request, 'main.html', {'data': data, 'authuser': AUTH_USER_MODEL})


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password'],
                fieldname=data['fieldname'],
                age=data['age']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
        return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, 'signupform.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, 'signupform.html', {"form": form})


def logout_view(request):
    # requests to logout
    logout(request)
    # Redirects to the login page.
    return HttpResponseRedirect(reverse('login'))
