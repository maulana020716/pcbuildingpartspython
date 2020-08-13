
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)


class HomeView(TemplateView):
    template_name = "index.html"
