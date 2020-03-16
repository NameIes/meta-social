from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError("Email is already in use!")


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False

    class Meta:
        model = Profile
        fields = ('job', 'biography', 'gender', 'country', 'birth')
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'})
        }
        labels = {
            "job": "Работа",
            "biography": "Биография",
            "gender": "Пол",
            "country": "Страна",
            "birth": "Дата рождения"
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class AddMessage(forms.Form):
    message = forms.CharField(max_length=250,
                              required=True,
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Сообщение',
                                  'style': 'width: 90%; height: 10%;'

                              }))
