from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from simple_search import search_filter
from django.utils import timezone
from .models import Profile
from PIL import Image


from .models import Friend, Post, FriendshipRequest
from .forms import ProfileUpdateForm, UserUpdateForm


def get_menu_context(page, pagename):
    available_pages = [
        'profile',
        'newsfeed',
        'friends',
    ]

    if page not in available_pages:
        raise KeyError

    context = {
        'page': page,
        'messages_count': 0,  # TODO: Вносить количество не прочитанных сообщений
        'pagename': pagename,
    }

    return context


@login_required
def index(request):
    context = get_menu_context('newsfeed', 'Главная')
    context['pagename'] = "Главная"
    return render(request, 'index.html', context)


@login_required
def profile(request, user_id):
    if not User.objects.filter(id=user_id).exists():
        raise Http404()

    context = get_menu_context('profile', 'Профиль')
    context['profile'] = Profile.objects.get(user=user_id)
    user_item = User.objects.get(id=user_id)
    context['c_user'] = user_item

    return render(request, 'profile/profile_page.html', context)


class ImageManage():
    def __init__(self, user_id, profile, image):
        self.fs = FileSystemStorage()
        self.path = 'avatars/users/' + str(user_id) + '.'
        self.profile = profile
        self.image = image

    def remove_old_avatar(self):
        if self.profile.avatar.name != 'avatars/users/0.png':
            self.fs.delete(self.profile.avatar.path)

    def save_avatar(self):
        self.fs.save(self.path, self.image)
        self.profile.avatar = self.path
        self.profile.save()

    def resize_image(self):
        self.image = Image.open(self.profile.avatar)
        size = (200, 200)
        self.image = self.image.resize(size, Image.ANTIALIAS)
        self.image.save(self.profile.avatar.path)

    def process_img(self):
        if self.image.size <= 5000000 and self.image.content_type.split('/')[0] == 'image':
            img_extension = self.image.name.split('.')[1]
            self.path += img_extension
            self.remove_old_avatar()
            self.save_avatar()
            self.resize_image()


class EditProfile(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = 'profile/edit_profile.html'
        self.profile = None

    def post(self, request, **kwargs):

        user_form = UserUpdateForm(request.POST, instance=User.objects.get(id=kwargs['user_id']))
        self.profile = Profile.objects.get(user=kwargs['user_id'])

        self.profile.show_email = False if request.POST.get('show_email') is None else True

        try:
            img_manage = ImageManage(kwargs['user_id'], self.profile, request.FILES['avatar'])
            img_manage.process_img()
        except Exception:
            pass

        profile_form = ProfileUpdateForm(request.POST, instance=Profile.objects.get(user=kwargs['user_id']))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/accounts/profile/' + str(kwargs['user_id']))

    def get(self, request, **kwargs):
        context = get_menu_context('profile', 'Редактирование профиля')
        context['profile'] = Profile.objects.get(user=kwargs['user_id'])
        context['uedit'] = User.objects.get(id=kwargs['user_id'])
        context['user_form'] = UserUpdateForm(instance=User.objects.get(id=kwargs['user_id']))
        context['profile_form'] = ProfileUpdateForm(instance=Profile.objects.get(user=kwargs['user_id']))

        return render(request, self.template_name, context)


@login_required
def friends_list(request, user_id):
    context = get_menu_context('friends', 'Список друзей')
    context['c_user'] = User.objects.get(id=user_id)

    return render(request, 'friends/friends_list.html', context)


@login_required
def friends_search(request):
    context = get_menu_context('friends', 'Поиск друзей')
    if request.method == 'POST':
        if request.POST.get('name'):
            query = request.POST.get('name')
            search_fields = ['username', 'first_name', 'last_name']

            matches = User.objects.filter(search_filter(search_fields, query)).exclude(id=request.user.id)
            context['matches'] = matches

    return render(request, 'friends/search.html', context)


@login_required
def friends_requests(request):
    context = get_menu_context('friends', 'Заявки в друзья')
    context['pagename'] = "Заявки в друзья"
    return render(request, 'friends/requests.html', context)


@login_required
def friends_blacklist(request):
    context = get_menu_context('friends', 'Черный список')
    return render(request, 'friends/blacklist.html', context)


@login_required
def post_new(request):
    if request.method == "POST":
        if request.POST.get('text'):
            post = Post(
                text=request.POST.get('text'),
                user=request.user,
            )
            post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def send_friendship_request(request, user_id):
    # TODO: Запретить повторяющиеся заявки, и себе
    if request.method == 'POST':
        item = FriendshipRequest(
            from_user=request.user,
            to_user=User.objects.get(id=user_id),
            already_sent=True
        )

        item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def accept_request(request, request_id):
    if request.method == 'POST':
        request_item = FriendshipRequest.objects.get(id=request_id)
        friends_item = Friend(
            from_user=request_item.from_user,
            to_user=request_item.to_user,
        )
        friends_item.save()
        request_item.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_friend(request, user_id):
    if request.method == 'POST':
        friend = User.objects.get(id=user_id)
        try:
            friend_item = Friend.objects.get(to_user=request.user, from_user=friend)
        except:
            friend_item = Friend.objects.get(to_user=friend, from_user=request.user)
        friend_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def blacklist_add(request, user_id):
    if request.method == 'POST':
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def blacklist_remove(request, user_id):
    if request.method == 'POST':
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def chat(request):
    context = {}
    context['c_user'] = User.objects.get(id=request.user.id)

    return render(request, 'chat/chat.html', context)


def send_message(request, user_id):
    context = {}
    context['c_user'] = User.objects.get(id=request.user.id)

    return render(request, 'chat/message.html', context)