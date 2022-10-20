from django.urls import path
from .views import HomeView, PostDetailView, NewPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('new_post/', NewPostView.as_view(), name="new_post"),
]
