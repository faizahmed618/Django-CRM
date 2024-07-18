from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from APP1 import models
from . import forms

class Agentlistview(generic.ListView):
    template_name = "Agent/agent-list.html"
    context_object_name = "agents"
    
    def get_queryset(self):
        return models.Agent.objects.all()
    
class Agentcreateview(generic.CreateView):
    template_name = "Agent/agent-create.html"
    form_class = forms.create_form_agent
    
    def get_success_url(self):
        return reverse("AgentNameSpace:agent-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(Agentcreateview, self).form_valid(form)
    
def check(request):
    agent = models.Agent.objects.get(id=1)
    leads = agent.lead_set.all()
    print(agent.leads[0].firstName) # Agent has multiple leads thats why simple "agent.lead.firstName" doesn't exist.
    return render(request, "landing.html")

