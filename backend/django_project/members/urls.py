from django.urls import path
from .views import home, details

urlpatterns = [
    path('members/', home, name = 'home'),
    path('members/details/<int:id>', details, name='details')
]
