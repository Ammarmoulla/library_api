from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_filter = ["title", "author"]
    search_fields = ["title", "author"]
    