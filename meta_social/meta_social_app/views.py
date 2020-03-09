from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import Friend, Posts, Audio


@login_required
def index(request):
    user = User.objects.exclude(id=request.user.id)

    context = {
        'user': user,
        'audio':  Audio.objects.all()
    }
    #friends =Friend.objects.get(current_user=request.user, )
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


@login_required
def music(request):
    user = User.objects.exclude(id=request.user.id)

        # Load documents for the list page
    a=Audio.objects.all()
    d=['/'+str(i.sound.url) for i in a]
    for i in range(len(a)):
        a[i].url=d[i]
    context = {
        'user': user,
        'audio': a

    }
    # friends =Friend.objects.get(current_user=request.user, )
    return render(request, 'music.html', context)

@login_required
def add_sound(request):
    user = User.objects.exclude(id=request.user.id)
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():

            audio=Audio(sound=form.cleaned_data.get("file"),name=form.cleaned_data.get("name"),author=form.cleaned_data.get("author"),avatar=form.cleaned_data.get("avatar"))

            audio.save()
            # Redirect to the document list after POST

          # A empty, unbound form

        # Load documents for the list page

    context = {
        'user': user,

        'form': form
    }
    # friends =Friend.objects.get(current_user=request.user, )
    return render(request, 'add_sound.html', context)



