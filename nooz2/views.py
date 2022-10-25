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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context
        

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

    def get_context_data(self, *args, **kwargs):
            category_menu = Category.objects.all()
            context = super(CategoryView, self).get_context_data(*args, **kwargs)
            context ["category_menu"] = category_menu
            return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context

class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    #fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(NewPostView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context

class EditPostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #  fields = ['title', 'title_tag', 'body']
    def get_context_data(self, *args, **kwargs):
            category_menu = Category.objects.all()
            context = super(EditPostView, self).get_context_data(*args, **kwargs)
            context ["category_menu"] = category_menu
            return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
                category_menu = Category.objects.all()
                context = super(DeletePostView, self).get_context_data(*args, **kwargs)
                context ["category_menu"] = category_menu
                return context
