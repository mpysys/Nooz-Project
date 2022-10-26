from django.urls import path, re_path
from .views import HomeView, PostDetailView, NewPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('new_post/', NewPostView.as_view(), name="new_post"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
]
