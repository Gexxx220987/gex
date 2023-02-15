from django.forms import ModelForm, widgets, ModelChoiceField, CharField, Select, DateTimeField, ModelMultipleChoiceField, Textarea
from .models import Post, Author, Category, CHOICES_POST_NEWS


class PostForm(ModelForm):
    author = ModelChoiceField(queryset=Author.objects.all(), label='Автор:')
    post_or_news = CharField(label='Статья или Новость:', widget=Select(choices=CHOICES_POST_NEWS))
    category = ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all())
    title = CharField(label='Заголовок', max_length=255)
    text = CharField(label='Текст статьи', widget=Textarea())

    class Meta:
        model = Post
        fields = [
            'author', 'category', 'title', 'text', 'post_or_news',
        ]
