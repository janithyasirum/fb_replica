# coding: utf-8

import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


def get_posts(posts, user):

    posts_list = []
    for post in posts:
        comments_list = []
        for comment in post.comments.all():
            comments_list.append(get_comment_dict(comment, user))
        post_dict = get_post_dict(post, user)
        post_dict['comments'] = comments_list
        posts_list.append(post_dict)

    return posts_list


def get_post_dict(post, user):
    post_dict = dict()

    post_dict['id'] = post.pk
    post_dict['user'] = post.user
    post_dict['description'] = post.description
    post_dict['date'] = post.date
    post_dict['images'] = post.images
    post_dict['videos'] = post.videos
    post_dict['files'] = post.files
    post_dict['likes_count'] = post.likes_count
    if not user.is_anonymous:
        post_dict['can_like'] = not (post.likes.filter(user=user).exists())

    return post_dict


def get_comment_dict(comment, user):
    comment_dict = dict()

    comment_dict['id'] = comment.pk
    comment_dict['user'] = comment.user
    comment_dict['description'] = comment.description
    comment_dict['date'] = comment.date
    comment_dict['likes_count'] = comment.likes_count
    if not user.is_anonymous:
        comment_dict['can_like'] = not (comment.likes.filter(user=user).exists())

    return comment_dict

