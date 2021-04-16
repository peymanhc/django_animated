from django.shortcuts import render, redirect
from django.contrib import messages
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
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.success(request, 'your message Sended')
            form.save()

    return render(request, 'blog/frontpage.html', {
        'posts': posts,
        'abouts':abouts,
        'myteams':myteams,
        'gallerys':gallerys,
        'videos':videos,
        'form':form
        })
 
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post}) 