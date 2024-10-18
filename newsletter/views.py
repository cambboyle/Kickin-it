from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from .forms import NewsletterSubscriptionForm
from .models import Subscriber

@login_required
def subscribe(request):
    """ A view to subscribe to newsletter """
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if email != request.user.email:
                messages.error(request, "Please use the email linked to your account.")
            else:
                subscriber, created = Subscriber.objects.get_or_create(user=request.user)

                if created:
                    subscriber.email = email
                    subscriber.save()

                    messages.success(request, "You've been subscribed to our newsletter!")

                    subject = render_to_string(
                        'newsletter/subscribe_confirmation_subject.txt',
                    )

                    body = render_to_string(
                        'newsletter/subscribe_confirmation_body.txt',
                        {'contact_email': settings.DEFAULT_FROM_EMAIL, 'subscriber_email': email}
                    )

                    send_mail(
                        subject.strip(),
                        body,
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                else:
                    messages.info(request, "You're already subscribed to our newsletter.")

            return redirect('home')

    return redirect('home')

def unsubscribe(request, email):
    """A view to unsubscribe from newsletter"""
    subscriber = Subscriber.objects.filter(email=email).first()

    if request.method == 'POST':
        if subscriber:
            subscriber.delete()
            messages.success(request, "You have been unsubscribed from our newsletter.")
        else:
            messages.error(request, "The email address is not subscribed to our newsletter.")
        return render(request, 'newsletter/unsubscribe_confirmation.html')

    return render(request, 'newsletter/unsubscribe.html', {'subscriber': subscriber})


def unsubscribe_confirmation(request):
    """ A view to show unsubscribe confirmation page """
    return render(request, 'newsletter/unsubscribe_confirmation.html')
