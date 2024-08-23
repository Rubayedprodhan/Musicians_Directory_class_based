from django.urls import path
from .views import AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('new/', AlbumCreateView.as_view(), name='create_album'),
    path('edit/<int:pk>/', AlbumUpdateView.as_view(), name='album_edit'),
    path('delete/<int:pk>/', AlbumDeleteView.as_view(), name='album_delete'),
]
