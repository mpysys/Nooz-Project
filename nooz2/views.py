from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-timestamp']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #  fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
