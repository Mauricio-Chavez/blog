from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView.as_view(), name='about'),
    path('list/',views.PostListView.as_view(),name='list'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('new/',views.PostCreateView.as_view(),name='new'),
    path('edit/<int:pk>/',views.PostUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
]