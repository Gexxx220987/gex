from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory
# new
# from django.db.models.signals import post_save
# from django.core.mail import send_mail
# from django.contrib.auth.models import User



def send_notifications(prevew, pk, title, subscribers):

    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': prevew,
            'link': f'{settings.SITE_URL}/news/{pk}',
            #'link': f'http://127.0.0.1:8000/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':

        print('Я сигнал!')

        categories = instance.category.all()
        print(f'{categories = }')

        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()
        print(f'{subscribers = }')

        subscribers = [s.email for s in subscribers]
        print(f'{subscribers = }')

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)

# # новое
# @receiver(post_save, sender=User)
# def notify_managers_posts(sender, instance, created, **kwargs):
#     if created:
#         title = f'news_portal. Пользователь {instance.username} зарегистрирован.'
#         message = f'Добрый день, {instance.username}!\n' \
#                   f'Команда NewsPaper благодарит вас за регистрацию на нашем портале.\n' \
#                   f'Теперь вам доступны: личный кабинет и возможности писать комментарии,' \
#                   f' или стать автором и написать статью.'
#     else:
#         title = f'NewsPaper. Данные пользователя {instance.username} изменены.'
#         message = f'Добрый день, {instance.username}!\n' \
#                   f'Ваши персональные данные были изменены. Подробнее в личном кабинете , на сайте.'
#     send_mail(
#         subject=title,
#         message=message,
#         from_email=settings.SERVER_EMAIL,
#         recipient_list=[instance.email,]
#     )
