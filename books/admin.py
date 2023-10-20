from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "isbn"]
    list_filter = ["title", "author"]
    search_fields = ["title", "body"]