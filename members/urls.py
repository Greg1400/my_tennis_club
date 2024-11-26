from django.urls import path
from . import views

"""URL Configruation for the application
"""
urlpatterns = [
    path('', views.main, name='main'), # root URL mapped to main views
    path('members/', views.members, name='members'), # URL memebers mapped to members views
    path('members/details/<slug:slug>', views.details, name='details'), # URL mapped to details view containing the details of the specific ID passed in the parameter
    path('testing/', views.testing, name='testing'), # URL mapped to testing views
]