from celery import shared_task
# from .models import Order
# import datetime
import time
# from celery import shared_task
# from news.models import Category, Post
# from .config import newsletter_sender


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")






# @shared_task
# def complete_order(oid):
#     order = Order.objects.get(pk = oid)
#     order.complete = True
#     order.save()




#Новое
# @shared_task
# def mailing():
#     list_recipients = []
#     date_from = datetime.datetime.now() - datetime.timedelta(days=7)
#     for category in Category.objects.all():
#         list_recipients.clear()
#         for user in category.subscribed_users.all():
#             list_recipients.append(user.email)
#         posts = Post.objects.filter(category=category, date_time_in__gte=date_from)
#         newsletter_sender(list_recipients, category.name, posts)
