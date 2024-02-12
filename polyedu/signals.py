from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from datetime import datetime, timedelta, timezone
from .models import Article, Profile

@receiver(post_save, sender=Article)
def add_points_to_user(sender, instance, created, **kwargs):
    if created:
        # The article was just created, so let's add points to the user's profile
        user_profile = instance.user.profile
        user_profile.points += 50  # You can adjust the points as needed
        user_profile.save()

@receiver(user_logged_in)
def add_daily_points(sender, request, user, **kwargs):
    user_profile = Profile.objects.get(user=user)
    
    # Get the user's last login timestamp
    last_login = user.last_login
    
    # Check if the last login was more than 24 hours ago
    now = datetime.now(timezone.utc)
    if now - last_login > timedelta(days=1):
        user_profile.points += 5  # Add 5 points on the first login of the day
        user_profile.save()

@receiver(m2m_changed, sender=Article.likes.through)
def update_user_points(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        # Update the user's points for each like added
        user = instance.user
        user.profile.points += 10 * len(pk_set)  # Adjust points as needed
        user.profile.save()
    elif action == "post_remove":
        # Update the user's points for each like removed
        user = instance.user
        user.profile.points -= 10 * len(pk_set)  # Adjust points as needed
        user.profile.save()

@receiver(m2m_changed, sender=Profile.follows.through)
def update_follower_points(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        # Add 25 points for each follower added
        instance.points += 25 * len(pk_set)  # Adjust points as needed
    elif action == "post_remove":
        # Remove 25 points for each follower removed
        instance.points -= 25 * len(pk_set)  # Adjust points as needed
    
    instance.save()