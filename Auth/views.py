from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from timeline.models import Post
from FB_Replica.shared_utils import get_posts


def index(request):
    posts = Post.objects.all().order_by('-date')
    context = {"posts_list": get_posts(posts, request.user)}
    return render(request, 'index.html', context)


def signup_view(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('email')
    password = request.POST.get('password')

    if username is None or password is None or first_name is None or last_name is None:
        messages.add_message(request, messages.ERROR, "Please provide first_name, last_name, email and password")
        return redirect('/')
        # return render(request, 'index.html')
    try:
        user = User.objects.create_user(username=username, email=username, first_name=first_name, last_name=last_name,
                                        password=password)

        return login_view(request=request)

    except IntegrityError as e:
        if 'UNIQUE constraint' in e.args[0]:  # or e.args[0] from Django 1.10 else e.message
            messages.add_message(request, messages.ERROR, "Email already registered")
            return redirect('/')
            # return render(request, 'index.html')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong")
            return redirect('/')
            # return render(request, 'index.html')


@csrf_exempt
def login_view(request):
    username = request.POST.get('email')
    password = request.POST.get('password')

    if username is None or password is None:
        messages.add_message(request, messages.ERROR, "Please provide email and password")
        return redirect('/')
        # return render(request, 'index.html')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # messages.add_message(request, messages.SUCCESS, "You are logged in")
        return redirect('/')
        # return HttpResponseRedirect("/")

    else:
        messages.add_message(request, messages.ERROR, "Unable to authenticate this user")
        return redirect('/')
        # return render(request, 'index.html')


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You are logged out")
    return redirect('/')
    # return HttpResponseRedirect("/")


@login_required(login_url='/')
def members_view(request):
    members = User.objects.filter(is_superuser=False, ).exclude(email__iexact=request.user.email)
    context = {"members_list": members}
    return render(request, 'members.html', context)


@login_required(login_url='/')
def profile_view(request, user_id):
    if user_id is None:
        messages.add_message(request, messages.ERROR, "Please provide id of the user")
        return redirect('/')
        # return render(request, 'index.html')

    try:
        user = User.objects.get(pk=user_id)
        # user.prefetch_related('profile')
        context = {"user_obj": user}
        return render(request, 'profile.html', context)

    except User.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Unable to find this user")
        return redirect('/')
        # return render(request, 'index.html')


def edit_profile(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    if request.method == 'POST':
        image = request.FILES.get('image')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        if image:
            profile.image = image

        profile.user.first_name = first_name
        profile.user.last_name = last_name
        profile.city = city
        profile.state = state
        profile.gender = gender
        profile.birth_date = dob
        profile.user.save()

        return redirect(("/profile/%d/" % profile.user_id))
        # return HttpResponseRedirect("/profile/%d/" % profile.user_id)

    else:
        pass

    context = {"profile": profile}

    return render(request, 'edit_profile.html', context)
