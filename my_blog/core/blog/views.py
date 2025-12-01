from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Imageslides
from django.shortcuts import get_object_or_404

# Create your views here.

class HomeView(ListView):
    model = Post   
    context_object_name = 'posts'
    paginate_by = 10
    #template_name = 'blog/home.html'
 

    def get_template_names(self):
        if self.request.htmx:
            return 'blog/components/post_list.html'
        return 'blog/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add published slides to template context
        context['imageslides'] = Imageslides.objects.filter(status='published')
        return context
    
def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    related = Post.objects.filter(author=post.author, status='published')[:3]
    return render(request, 'blog/single.html', {'post': post, 'related': related})