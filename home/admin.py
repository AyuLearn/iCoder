from django.contrib import admin
from .models import Contact, Post, Comments

# Register your models here.
admin.site.register((Contact, Post, Comments))