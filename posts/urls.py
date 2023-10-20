from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewset, basename="users")
router.register(r'', views.PostViewset, basename="posts")

urlpatterns = [
    # path("", views.PostList.as_view(), name="post_list"),
    # path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
]

urlpatterns += router.urls
