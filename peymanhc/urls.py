from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
]

urlpatterns += staticfiles_urlpatterns()