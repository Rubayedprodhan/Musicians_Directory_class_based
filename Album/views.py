from .forms import AlbumForm
from django.urls import reverse_lazy
from django.views.generic import  CreateView, UpdateView, DeleteView
from .models import  Album
from .forms import AlbumForm
from django.contrib import messages
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'create_album.html'
    success_url = reverse_lazy('homepage')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'create_album.html'
    success_url = reverse_lazy('homepage')
   
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('homepage')


