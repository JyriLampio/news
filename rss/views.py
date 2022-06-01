from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from . import models
import feedparser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class RssListView(LoginRequiredMixin, ListView):
    #model = models.Rss
    def get_queryset(self):
        return models.Rss.objects.filter(owner=self.request.user)

#class RssDetailView(LoginRequiredMixin, DetailView):
	#model = models.Rss

class RssCreateView(LoginRequiredMixin, CreateView):
	model = models.Rss
	#fields = "__all__"
	fields = ['website', 'category']
	success_url = "/rss/"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class RssUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Rss
	#fields = "__all__"
	fields = ['website', 'category']
	success_url = "/rss/"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)
		
class RssDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Rss
	success_url = "/rss/"
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

#Authentication
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login/"

def index(request, pk):
    #if request.GET.get('website'):
    website = request.GET['website']
    category = request.GET['category']
    url = 'https://www.'+website+'.fi/rss/'+category+'.xml'
    parsedxml = feedparser.parse(url)
    return render(request, 'rss/index.html', { 'feed' : parsedxml, })
