from django.contrib import admin

# Register your models here.
from .models import Job,User

admin.site.register(Job)
admin.site.register(User)
