from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from areacode.models import Province, Regency, District, Village


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    province = models.ForeignKey(Province,
                                 on_delete=models.CASCADE,
                                 related_name='provinces', null=True)
    regency = models.ForeignKey(Regency,
                                on_delete=models.CASCADE,
                                related_name='regencies', null=True)
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE,
                                 related_name='districts', null=True)
    village = models.ForeignKey(Village,
                                on_delete=models.CASCADE,
                                related_name='villages', null=True)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return str(self.user_profile)
