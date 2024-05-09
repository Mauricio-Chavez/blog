from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.PostListView.as_view(),name='list'),
    path('drafts/',views.DraftListView.as_view(),name='drafts'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('new/',views.PostCreateView.as_view(),name='new'),
    path('edit/<int:pk>/',views.PostUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
]