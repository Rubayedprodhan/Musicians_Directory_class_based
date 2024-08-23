from django.urls import path
from .views import MusicianCreateView, MusicianUpdateView, MusicianDeleteView

urlpatterns = [
    path('new/', MusicianCreateView.as_view(), name='create_musicians'),
    path('edit/<int:pk>/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('delete/<int:pk>/', MusicianDeleteView.as_view(), name='musician_delete'),
]
