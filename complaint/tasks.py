# from time import sleep
# from celery import shared_task
# from django.core.mail import send_mail
#
#
# @shared_task()
# def send_feedback_email_task(message):
#     email_from = settings.EMAIL_HOST_USER
#     recipient = ['tusharsingla2822@gmail.com', ]
#     sleep(20)
#     send_mail(
#         "Your Feedback",
#         f"\t{message}\n\nThank you!",
#         email_from,
#         recipient,
#         fail_silently=False,
#     )
