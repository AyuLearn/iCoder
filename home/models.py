from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=900)
    message = models.TextField()

    def __str__(self):
        return self.name +  ' - ' + self.email

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=700)
    category = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='post_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dt = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title + ' by ' + self.author.first_name + ' ' + self.author.last_name

class Comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.comment[0:18] + '...' + self.user.first_name + ' ' + self.user.last_name


    