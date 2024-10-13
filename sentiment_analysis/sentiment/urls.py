from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # This will map the home view to the root URL
]
