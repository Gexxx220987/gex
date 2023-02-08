from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory



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
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     print(instance)
#     if kwargs['action'] == 'post_add':
#         print('Прошёл')
#         categories = instance.category.all()
#         print(categories, ' cate')
#         subscribers: list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers)
