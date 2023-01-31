# from django.db.models.signals import
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import UserResponse
from django.db.models.signals import post_save,pre_save


@receiver(pre_save, sender=UserResponse)
def my_handler(sender,instance, created, **kwargs):
    if instance.status:
        mail = instance.author.email
        send_mail(
            'subject here',
            'Here is the message',
            'host@mail.ru',
            [mail],
            fail_silently=False,
        )
    else:
        mail = instance.article.author.email
    send_mail(
        'subject here',
        'Here is the message',
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )
