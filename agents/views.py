import random
from django.views import generic
from django.shortcuts import reverse
from leads.models import Agent
from .mixins import LoginRequiredMixin
from django.core.mail import send_mail
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = "agents/agents_lists.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organiser = False
        user.is_agent = True
        user.set_password(f'{random.randint}')
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="Bu agent yaratilingan",
            message="Yangi agent yarat",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agents_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")