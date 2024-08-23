from django.shortcuts import render, redirect
from .forms import MusicianForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Musician

class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('homepage')

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('homepage')

class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'musician_delete.html'
    success_url = reverse_lazy('homepage')
