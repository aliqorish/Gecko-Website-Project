from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Day

@receiver(post_save, sender=User)
def intiateDays(sender, instance, created, **kwargs):
    if created:
        for dayvalue, _ in Day.daysofweek.choices:
            Day.objects.create(user=instance, day=dayvalue)

