"""
Meta social music views
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from core.views import MetaSocialView

from .forms import UploadMusicForm
from user_profile.models import Profile
from user_profile.models import PlayPosition


class MusicViews:
    """
    Class containing music functionality and representation
    """
    class MusicList(MetaSocialView):
        """
        Music list representaion
        """
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.template_name = 'music/music_list.html'

        def get(self, request, custom_url):
            """
            Processing get request
            """
            context = self.get_menu_context('music', 'Музыка')
            context['music_pages'] = 'my_list'

            context['c_user'] = get_object_or_404(Profile, custom_url=custom_url).user
            context['music_list'] = context['c_user'].profile.get_music_list()

            return render(request, self.template_name, context)

        def post(self, request, custom_url):
            """
            Replace order
            """
            str_arr = request.POST.get('music_order')
            arr = list(map(int, str_arr.split(',')))
            c_user = get_object_or_404(Profile, custom_url=custom_url).user
            c_user.profile.change_playlist(arr)
            return HttpResponse('Success')


    class MusicUpload(MetaSocialView):
        """
        Music upload and representation
        """
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.template_name = 'music/music_upload.html'

        def post(self, request):
            """
            Processing post request. Save uploaded music
            """
            form = UploadMusicForm(request.POST, request.FILES)
            if form.is_valid():
                music = form.save()
                playpos = PlayPosition(position=music,
                                       plist=request.user.profile)
                playpos.add_order()
                playpos.save()

            return redirect('/accounts/profile/{}/music/'.format(request.user.profile.custom_url))

        def get(self, request):
            """
            Processing get request
            """
            context = self.get_menu_context('music', 'Загрузка музыки')
            context['music_pages'] = 'upload'

            context['form'] = UploadMusicForm()

            return render(request, self.template_name, context)
