from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import mail_managers


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user

# class CustomSignupForm(SignupForm):
#    def save(self, request):
#        user = super().save(request)
#        common_users = Group.objects.get(name="author")
#        user.groups.add(common_users)
#        return user


User = get_user_model()

class PostForm(forms.ModelForm):
    required_css_class = 'my-custom-class'
    title = forms.CharField(max_length=40)

    class Meta:
        model = Post
        fields = ['title', 'author', 'post_type', 'category', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control"})
        self.fields['title'].label = "Заголовок публикации"
        self.fields['title'].widget.attrs.update({'placeholder': "Введите название"})
        self.fields['text'].label = "Текст публикации"
        self.fields['text'].widget.attrs.update({'placeholder': "Введите текст здесь"})

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Текст статьи не должен быть идентичен заголовку."
            )
        return cleaned_data


class Registration(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
