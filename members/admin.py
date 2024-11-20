from django.contrib import admin
from .models import Member

"""The use of 'admin.py' is to display the models
    in the Django Admin Panel.
"""
admin.site.register(Member)
