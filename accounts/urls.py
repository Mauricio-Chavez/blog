from django.urls import path
from .views import SignUpView  # Asegúrate de que tu vista esté importada

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # Agrega esta línea
]