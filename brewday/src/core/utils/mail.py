from django.conf import settings
from django.core.mail import EmailMessage


def send_welcome_mail(user):
    message = EmailMessage(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
        subject='[BrewDay Platform] Welcome {}'.format(user.profile.name),
    )

    message.template_name = 'emails/welcome.html'
    message.global_merge_vars = {'user': user}
    message.merge_language = "handlebars"
    message.send(fail_silently=True)
