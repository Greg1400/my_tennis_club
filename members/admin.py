from django.contrib import admin
from .models import Member

"""The use of 'admin.py' is to display the models
    in the Django Admin Panel.
"""

class MemberAdmin(admin.ModelAdmin):
    """Class which allow us to display specific fields of the Members from 
        the members list
    """
    # tuple 
    list_display = ("firstname", "lastname", "joined_date")
    prepopulated_fields = {"slug": ("firstname", "lastname")}    
    
admin.site.register(Member, MemberAdmin)
