from django.db import models
from django.contrib.auth.models import User

CHOICES_POST_NEWS = [
    ('POST', 'Статья'),
    ('NEWS', 'Новость')
]


# Модель автора с методом подсчета его рейтинга
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def update_rating(self):
        summ_rating_posts = 0  # суммарный рейтинг каждой статьи автора;
        summ_rating_comments_at_post = 0  # суммарный рейтинг всех комментариев к статьям автора;
        summ_rating_comments = 0  # суммарный рейтинг всех комментариев автора;
        for element in self.posts.all():
            summ_rating_posts += int(element.rating_post)
            for _ in element.comments_p.all():
                summ_rating_comments_at_post += int(_.rating_comment)
        for element in self.user.comments_u.all():
            summ_rating_comments += int(element.rating_comment)
        self.rating_author = (3 * summ_rating_posts) + summ_rating_comments + summ_rating_comments_at_post
        self.save()

    def __str__(self):
        return f'Автор: {self.user.username}'


# Модель категорий для систематизации статей и новостей
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribed_users = models.ManyToManyField(User, through='SubscribedUsersCategory')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.name}'


# Модель Статьи(или новости) с методами like и dislike для изменения рейтинга статьи
# Метод preview показывает первые 124 символа статьи
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    post_or_news = models.CharField(max_length=4, choices=CHOICES_POST_NEWS, default='POST')
    date_time_in = models.DateTimeField(auto_now_add=True, )
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    def __str__(self):
        return f'Статья: {self.title}. (Рейтинг: {self.rating_post}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return (self.text[:124] + '...')


# Модель реализующая связь Многие ко Многим
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class SubscribedUsersCategory(models.Model):
    subscribed_users = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Модель комментария с методами like и dislike для изменения рейтинга комментария
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_p')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_u')
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

