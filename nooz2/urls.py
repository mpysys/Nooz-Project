from django.urls import path
from .views import HomeView, PostDetailView, NewPostView, EditPostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('new_post/', NewPostView.as_view(), name="new_post"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
]
