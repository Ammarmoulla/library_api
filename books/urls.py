from django.urls import path, include
from . import views
urlpatterns = [
    path("book_list/", views.BookAPIView.as_view(), name="book_list"),
]
