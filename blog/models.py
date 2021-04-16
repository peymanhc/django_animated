from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.FileField(null=True,blank=True,upload_to='')
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    class Meta:
        ordering = ['-date_added']

class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = ['title']

 
class MyTeam(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(null=True,blank=True,upload_to='')
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(null=True,blank=True,upload_to='')

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default="Video")
    video = models.FileField(null=True,blank=True,upload_to='')
 
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']