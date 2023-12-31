from django.shortcuts import render,get_list_or_404
from django.views.generic import  ListView,DetailView,CreateView,UpdateView
from django.views.generic import DeleteView
from .models import Post 
from django.contrib.auth.mixins  import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import get_object_or_404

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
     model=Post
     template_name='blog/home.html'
     context_object_name='posts'
     paginate_by=2 # this will only keep two pages on the screen.
     
     
class UserPostListView(ListView):
     model=Post
     template_name='blog/user_posts.html'
     context_object_name= 'posts'
     ordering=['-date_posted']
     paginate_by=2 # this will only keep two pages on the screen.
     
     
     def get_queryset(self):
            username = self.kwargs.get('username')
            user = get_object_or_404(User, username=username)
            return Post.objects.filter(author=user).order_by('-date_posted')

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        context['user'] = user
        return context

     
     
class PostDetailView(DetailView):
     model=Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
     model=Post    
     fields=['title','content']
     def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)     
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     model=Post  
     fields=['title','content']
     def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, 'Post updated successfully')
        return super().form_valid(form)  
     def test_func(self):
         post=self.get_object()
         if self.request.user==post.author:
              return True
         return False
     
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
        model=Post
        success_url='/'
        def test_func(self):
          post=self.get_object()
          if self.request.user==post.author:
               return True
           
          return False
      
      
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})