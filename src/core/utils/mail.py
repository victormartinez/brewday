from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_welcome_mail(user):
    html_content = render_to_string('emails/welcome.html', {'user': user})
    text_content = strip_tags(html_content)

    message = EmailMultiAlternatives(
        subject='[BrewDay Platform] Welcome {}'.format(user.profile.name),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
        body=text_content
    )

    message.attach_alternative(html_content, "text/html")
    message.send(fail_silently=True)
