from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import SignUpForm
import vk_api

from .models import *


def profile_page(request, user_id):
    if User.objects.filter(id=user_id).exists():
        user_item = User.objects.get(id=user_id)
        context = {'username': user_item.username}
    else:
        raise Http404()

    return render(request, 'profile.html', context)

def add_vk_captha(request):
    if request.is_ajax():
        print(request.POST)





def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации

    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device

def authorize_vk(login, password):
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        return error_msg

    print(vk_session)
    print('Authorized!')

@login_required
def add_vk(request):
    if request.is_ajax():
        attempt = LoginAttempt()
        attempt.user = User.objects.get(id=request.user.id)
        attempt.ok = False
        attempt.save()

        try:
            authorize_vk(request.POST.get('user'), request.POST.get('password'))
        except vk_api.exceptions.Captcha:
            print('Нужная капча')
            return HttpResponse('''<input id="capcha" name="capcha" placeholder="Введите капчу">
            <script>

            </script>
            <button>Отправить </button>''')







    return render(request,'add_vk.html')




@login_required
def index(request):
    context = {}

    return render(request, 'index.html', context)


class RegisterFormView(FormView):
    form_class = SignUpForm
    # Ссылка, на которую будет перенаправляться user
    # в случае успешной регистрации
    success_url = "#"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        for key in form.fields:
            print(form.fields[key])

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
