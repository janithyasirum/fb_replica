from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from FB_Replica.shared_utils import get_posts
from .models import *


@login_required(login_url='/')
def wall_post_view(request):
    description = request.POST.get('description')
    images = request.FILES.getlist('images')
    videos = request.FILES.getlist('videos')
    files = request.FILES.getlist('files')

    if description == '' and len(images) == 0 and len(videos) == 0 and len(files) == 0:
        messages.add_message(request, messages.ERROR, "Empty post can not be submitted")
        return redirect('/')
        # return render(request, 'index.html')
    try:
        post = Post.objects.create(description=description, user=request.user)

        for image in images:
            PostImages.objects.create(image=image, post=post)

        for video in videos:
            PostVideos.objects.create(video=video, post=post)

        for file in files:
            PostFiles.objects.create(file=file, post=post, file_name=file.name)

        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        return redirect('/', context)
        # return render(request, 'index.html', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def comment_post_view(request, post_id):
    description = request.POST.get('description')

    if description == '':
        messages.add_message(request, messages.ERROR, "Empty comment can not be submitted")
        return redirect('/')
        # return render(request, 'index.html')
    try:
        comment = PostComments.objects.create(description=description, post_id=post_id, user=request.user)
        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        return redirect('/', context)
        # return render(request, 'index.html', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def like_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        like, created = PostLikes.objects.get_or_create(post_id=post_id, user=request.user)
        if created:
            post.likes_count += 1
            post.save()

        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        # return render(request, 'index.html', context)
        return redirect('/', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def unlike_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        likes = PostLikes.objects.filter(post_id=post_id, user=request.user)

        if likes.count() > 0:
            post.likes_count -= 1
            post.save()

        likes.delete()

        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        return redirect('/', context)
        # return render(request, 'index.html', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def like_comment_view(request, comment_id):
    try:
        comment = PostComments.objects.get(pk=comment_id)
        like, created = CommentLikes.objects.get_or_create(comment_id=comment_id, user=request.user)
        if created:
            comment.likes_count += 1
            comment.save()

        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        return redirect('/', context)
        # return render(request, 'index.html', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def unlike_comment_view(request, comment_id):
    try:
        comment = PostComments.objects.get(pk=comment_id)
        likes = CommentLikes.objects.filter(comment_id=comment_id, user=request.user)

        if likes.count() > 0:
            comment.likes_count -= 1
            comment.save()

        likes.delete()

        posts = Post.objects.all().order_by('-date')
        context = {"posts_list": get_posts(posts, request.user)}
        return redirect('/', context)
        # return render(request, 'index.html', context)

    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return redirect('/')
        # return render(request, 'index.html')

