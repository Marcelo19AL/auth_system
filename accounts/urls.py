# accounts/urls.py
from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # Ruta para el registro
    path('login/', CustomLoginView.as_view(), name='login'),  # Ruta para iniciar sesión
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión
]
