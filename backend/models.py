from django.db import models

# Create your models here.
class Advocate(models.Model):
    profile_pic = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=50, unique = True)
    name = models.CharField(max_length=80)
    bio = models.TextField()
    work_at = models.CharField(max_length=100, blank=True, null=True)
    twitter_profile = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username