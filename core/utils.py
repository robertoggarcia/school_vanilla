from django.core.mail import send_mail


def send_my_email(subject, body, email_from, email_to):
    send_mail(
        subject,
        body,
        email_from,
        [email_to],
        fail_silently=False,
    )
