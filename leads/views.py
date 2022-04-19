from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from .forms import *

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = NewUserForm
    def get_success_url(self):
        return reverse('leads:leads-details')

class HomeView(TemplateView):
    template_name = 'home.html'

class ListView(LoginRequiredMixin, ListView):
    template_name = 'leads_lists.html'
    queryset = models.Lead.objects.all()
    context_object_name = 'leads'

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'details.html'
    queryset = models.Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/create.html'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:leads-details')

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/update.html'
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leads-details')

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/delete.html'
    queryset = models.Lead.objects.all()
    def get_success_url(self):
        return reverse('leads:leads-details')

def save_post(sender, instance, created, **kwargs):
    if created:
        models.UserProfile.objects.create(user=instance)


post_save.connect(save_post, sender=User)