from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

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

    