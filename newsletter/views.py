from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import NewsletterSubscriber

def subscribe_newsletter(request):
    """ Add a new subscriber to the newsletter """
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                send_mail(
                    'Subscription Confirmation',
                    'Thank you for subscribing to the Kickin\' It newsletter!',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Successfully subscribed to the newsletter!')
            else:
                messages.info(request, 'You are already subscribed')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('home')
