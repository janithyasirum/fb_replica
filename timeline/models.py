from django.db import models
from django.contrib.auth.models import User
from FB_Replica.shared_utils import UploadToPathAndRename
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.CharField(max_length=1024, null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, null=False, blank=True)
    likes_count = models.IntegerField(default=0)


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=UploadToPathAndRename('media/Images/Post/'), null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    footer = models.CharField(max_length=256, null=True, blank=True)


class PostVideos(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to=UploadToPathAndRename('media/Videos/Post/'), null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    footer = models.CharField(max_length=256, null=True, blank=True)


class PostFiles(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=UploadToPathAndRename('media/Files/Post/'), null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    footer = models.CharField(max_length=256, null=True, blank=True)


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, null=False, blank=True)
    likes_count = models.IntegerField(default=0)


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, null=False, blank=True)

    class Meta:
        unique_together = ('post', 'user')


class CommentLikes(models.Model):
    comment = models.ForeignKey(PostComments, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, null=False, blank=True)

    class Meta:
        unique_together = ('comment', 'user')

