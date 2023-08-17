from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    DeleteView, UpdateView, DetailView
from .models import Task
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
class TaskView(LoginRequiredMixin, FilterView):
    pass


class TaskCreateView(LoginRequiredMixin, CreateView):
    pass


class TaskUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    pass


class TaskDestroyView(LoginRequiredMixin):
    pass


class TaskShowView():
    pass
