from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from meta_social_app.models import Friend


@login_required
def index(request):
    user = User.objects.exclude(id=request.user.id)
    #friend = Friend.objects.all(current_user=request.user)
    #friends = friend.users.all()
    context = {
        'user': user,
        #'friends': friends,
    }
    return render(request, 'index.html', context)


@login_required
def profile(request, user_id):
    if not User.objects.filter(id=user_id).exists():
        raise Http404()

    context = {}

    user_item = User.objects.get(id=user_id)

    return render(request, 'profile.html', context)


@login_required
def profile_second(request, user_id):
    if not User.objects.filter(id=user_id).exists():
        raise Http404()

    context = {}

    user_item = User.objects.get(id=user_id)

    return render(request, 'profile_page.html', context)


@login_required
def add_friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    if operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return redirect('/')
