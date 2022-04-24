from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import *
from .forms import *

class SigupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class HomeView(TemplateView):
    template_name = "home.html"

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/leads_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user = self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation = user.userprofile,
                agent__isnull = True
            )
            context.update({
                "unassigned_leads": queryset
            })
        return context

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/leads_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"



class LeadCreateView(LoginRequiredMixin, CreateView):   
    template_name = "leads/leads_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

    # def form_valid(self, form):
    #     send_mail(
    #         subject="Bu lead yaratilingan",
    #         message="Yangi lead yarat",
    #         from_email="test@test.com",
    #         recipient_list=["test2@test.com"],
    #     )
    #     return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/leads_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/leads_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class AgentAssignView(LoginRequiredMixin, FormView):
    template_name = "leads/search-agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
                "request": self.request
            })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AgentAssignView, self).form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'leads/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)

        return queryset