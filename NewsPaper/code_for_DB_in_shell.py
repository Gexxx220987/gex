from news.models import *

# Создание пользователей
User.objects.create_user('user1')
User.objects.create_user('user2')
# Эти пользователи авторы
aut1 = Author(user=User.objects.get(pk=1))
aut1.save()
aut2 = Author(user=User.objects.get(pk=2))
aut2.save()
# Создание категорий статей
Category.objects.create(name='Фантастика')
Category.objects.create(name='Учебный материал')
Category.objects.create(name='Художественное повествование')
Category.objects.create(name='Научная статья')
# Создание статей
title = 'Вымирание смурфиков неизбежно'
text = 'Максимально аргумментированный текст про то, что все смурфики погибнут'
pos1 = Post(
    author=Author.objects.get(pk=1),
    post_or_news='POST',
    title=title,
    text=text
)
pos1.save()
pos2 = Post(author=aut1, post_or_news='POST', title='Python в современном мире', text='Рассказ о питоне с примерами кода')
pos2.save()
news1 = Post(author=aut2, post_or_news='NEWS', title='Объявление об отключении интернета', text='Даты и сроки отключения с извиненеиями')
news1.save()
# Создание связей статья - категории
PostCategory.objects.create(post=pos1, category=Category.objects.get(pk=1))
PostCategory.objects.create(post=pos2, category=Category.objects.get(pk=2))
PostCategory.objects.create(post=pos2, category=Category.objects.get(pk=4))
PostCategory.objects.create(post=news1, category=Category.objects.get(pk=1))
User.objects.create_user(username='user3')
# Создание комментариев
Comment.objects.create(post=pos1, user=User.objects.get(pk=3), text='Я считаю это глупостями')
Comment.objects.create(post=pos2, user=User.objects.get(pk=2), text='коммент')
Comment.objects.create(post=pos1, user=User.objects.get(pk=2), text='коммент2')
Comment.objects.create(post=news1, user=User.objects.get(pk=1), text='Неновижу отключения')
# Изменение рейтинга статей и комментариев
pos1.like()
pos2.dislike()
news1.like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()
# Обновление рейтинга авторов
aut1.update_rating()
aut2.update_rating()
# Выборка автора с самым высоким рейтингом
first = Author.objects.all().order_by('-rating_author').values('user__username', 'rating_author').first()
# Выборка лучшей статьи (на основании рейтинга)
best_post = Post.objects.all().order_by('-rating_post').first()
Post.objects.all().order_by('-rating_post').values('date_time_in', 'author__user__username', 'rating_post', 'title').first()
best_post.preview()
values_b_p = [_.values() for _ in Post.objects.all().order_by('-rating_post').values('date_time_in', 'author__user__username', 'rating_post', 'title').first()]
# Выборка всех комментариев к лучшей статье
comments_best_posts = Comment.objects.filter(post=best_post).values('date_time', 'user__username', 'rating_comment', 'text')
values_c_b_p = [_.values() for _ in comments_best_posts]


