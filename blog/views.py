from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class blog_article_content(DetailView):
    model = Post
    template_name = 'blog_article_content.html'

class create_post(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body', 'categories']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def economy_posts(request):
    posts = Post.objects.filter(categories__name='Økonomi')
    return render(request, 'økonomi.html', {'object_list': posts})

def school_posts(request):
    posts = Post.objects.filter(categories__name='Skole')
    return render(request, 'økonomi.html', {'object_list': posts})

def it_posts(request):
    posts = Post.objects.filter(categories__name='IT')
    return render(request, 'økonomi.html', {'object_list': posts})

def technology_posts(request):
    posts = Post.objects.filter(categories__name='Teknologi')
    return render(request, 'økonomi.html', {'object_list': posts})

def other_posts(request):
    posts = Post.objects.filter(categories__name='Annet')
    return render(request, 'økonomi.html', {'object_list': posts})