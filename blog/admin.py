from django.contrib import admin

from .models import Post
from .models import About
from .models import MyTeam
from .models import Gallery
from .models import Video

admin.site.register(Post)
admin.site.register(About) 
admin.site.register(MyTeam) 
admin.site.register(Gallery) 
admin.site.register(Video) 