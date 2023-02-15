from django.db.models.signals import post_save, m2m_changed
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.conf import settings
from .models import Post, Category
from .tasks import news_sender
import datetime

dict_message = dict()


@receiver(post_save, sender=Post)
def notify_managers_post(sender, instance, created, **kwargs):
    for category in instance.category.all():
        recipients = [user.email for user in category.subscribed_users.all()]
        if created:
            start_word = 'Новая'
        else:
            start_word = 'Обновлена'
        subject=f'На сайте NewsPaper {start_word.lower()} статья: {instance.title}'
        message=f'NewsPaper.\n{instance.title}:\n{instance.text[:30]}...\nПодробнее: http://127.0.0.1:8000/posts/{instance.id}'
        from_email=settings.SERVER_EMAIL
        news_sender.delay(subject, message, from_email, recipients)
        


@receiver(m2m_changed, sender=Post.category.through)
def notify_managers_posts(instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        html_content = render_to_string(
            'news/post_changes_create.html',
            {'post': instance, }
        )
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            recipients = [user.email for user in category.subscribed_users.all()]
            subject=f'На сайте NewsPaper новая статья: {instance.title}'
            message=f'NewsPaper.\n{instance.title}:\n{instance.text[:30]}...\nПодробнее: http://127.0.0.1:8000/posts/{instance.id}'
            from_email=settings.SERVER_EMAIL
            news_sender.delay(subject, message, from_email, recipients)
