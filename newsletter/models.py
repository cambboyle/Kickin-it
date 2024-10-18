from django.db import models

class NewsletterSubscriber(models.Model):
    """ Model for newsletter subscribers """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
