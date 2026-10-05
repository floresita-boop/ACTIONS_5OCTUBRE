

from django.contrib import admin
from django.urls import path
from app_actions.views import calculadora_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculadora_view),  # Esto hace que aparezca la calculadora al entrar a la página principal
]