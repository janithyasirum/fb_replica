from django.contrib import admin

# Register your models here.
from django.contrib import admin
from timeline.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(PostImages)
admin.site.register(PostVideos)
admin.site.register(PostFiles)
admin.site.register(PostComments)
admin.site.register(PostLikes)
admin.site.register(CommentLikes)
