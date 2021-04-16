from django.contrib import admin

from .models import Post
from .models import About
from .models import TeamMember

admin.site.register(Post)
admin.site.register(About)
admin.site.register(TeamMember) 