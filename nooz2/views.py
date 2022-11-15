from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

#landing page view and showcase articles
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-timestamp']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context
        
#like feature
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

#category view
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
            category_menu = Category.objects.all()
            context = super(CategoryView, self).get_context_data(*args, **kwargs)
            context ["category_menu"] = category_menu
            return context

#post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        #stuff corresponsds to various posts as many to many key
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        # Liked variable pass through to call
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context ["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

#new post view
class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    #fields = '__all__'
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(NewPostView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context
    
    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])

    def form_valid(self, form):
        form.instance.author = self.request.user
        # will save the form and redirect to the success_url
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


#add a category view
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context ["category_menu"] = category_menu
        return context

#edit post view
class EditPostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #  fields = ['title', 'title_tag', 'body']
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
            category_menu = Category.objects.all()
            context = super(EditPostView, self).get_context_data(*args, **kwargs)
            context ["category_menu"] = category_menu
            return context

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])

    def form_valid(self, form):
        form.instance.author = self.request.user
        # will save the form and redirect to the success_url
        return super().form_valid(form)


#delete a post view
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #category list for this specific view
    def get_context_data(self, *args, **kwargs):
                category_menu = Category.objects.all()
                context = super(DeletePostView, self).get_context_data(*args, **kwargs)
                context ["category_menu"] = category_menu
                return context
