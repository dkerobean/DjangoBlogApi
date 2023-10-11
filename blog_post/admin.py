from django.contrib import admin
from .models import Tag, Category, UserProfile, BlogPost

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(BlogPost)
