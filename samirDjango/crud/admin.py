from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.site_header  =  "Samir-Dave Crud Admin" 
admin.site.index_title  =  "Samir-Dave Crud Admin"

admin.site.register(Member)
