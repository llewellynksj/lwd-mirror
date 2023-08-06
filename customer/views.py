from django.shortcuts import render
from django.views import generic
# from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, UpdatePasswordForm, EditAccountSettingsForm
# EditProfileForm, PasswordUpdateForm, CreateProfileForm
from django.contrib.auth.models import User
# from .models import Customer
from django.http import HttpResponseRedirect


class AccountSettings(generic.UpdateView):
    form_class = EditAccountSettingsForm
    template_name = 'registration/account_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class UpdatePassword(PasswordChangeView):
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('profile')


class CustomerRegistration(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
