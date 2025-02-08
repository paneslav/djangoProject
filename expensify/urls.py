from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns ...
    path('dashboard/', views.dashboard, name='dashboard'),
]