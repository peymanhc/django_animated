from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post
from .models import About
from .models import MyTeam
from .models import Gallery
from .models import Video

def frontpage(request):
    posts = Post.objects.all()
    abouts = About.objects.all()
    myteams = MyTeam.objects.all()
    gallerys = Gallery.objects.all()
    videos = Video.objects.all()
    return render(request, 'blog/frontpage.html', {
        'posts': posts,
        'abouts':abouts,
        'myteams':myteams,
        'gallerys':gallerys,
        'videos':videos,
        })
 
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})