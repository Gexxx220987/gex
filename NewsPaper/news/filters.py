from django_filters import FilterSet, NumberFilter, DateFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Post, Author, Category
from django.forms.widgets import SelectDateWidget


class PostFilter(FilterSet):
    author_choice = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Автор:')
    date_time_in__gte = DateFilter(field_name='date_time_in', lookup_expr='gte', label='Дата публикации (не ранее):', widget=SelectDateWidget)
    category_choice = ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all(), label='Категория:')
    rating_post__gte = NumberFilter(field_name='rating_post', lookup_expr='gte', label='Рейтинг (не менее):')
    class Meta:
        model = Post
        fields = {
        }
