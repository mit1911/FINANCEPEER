from django import template
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from authy.forms import SignUpForm

def SignUpView(request):
    if request.method == "POST":

        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get('email')
            curr_user = User.objects.create_user(username=username, password=password, email=email)
            new_form = form.save(commit=False)
            new_form.user = curr_user
            new_form.save()
            return redirect('login')
    form = SignUpForm()
    return render(request, 'authy/Registration.html', {'form': form})
