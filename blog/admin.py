from django.contrib import admin

from .models import Post
from .models import About

admin.site.register(Post)
admin.site.register(About)