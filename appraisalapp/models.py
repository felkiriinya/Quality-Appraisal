from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
import cloudinary
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    locations = models.CharField(max_length=100)
    sector_focus = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    deal = models.CharField(max_length=100)
    bio = models.TextField()
    logo = CloudinaryField('image')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    # avg_rating = models.DecimalField(decimal_places=2, max_digits=3)
    # avg_mentorship = models.DecimalField(decimal_places=2, max_digits=3)
    # avg_hiring = models.DecimalField(decimal_places=2, max_digits=3)
    # avg_community = models.DecimalField(decimal_places=2, max_digits=3)
    # avg_corporate_fundraising = models.DecimalField(decimal_places=2, max_digits=3)
    # avg_fundraising = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_companies(cls):
        all_companies = cls.objects.all()
        return all_companies     

    def save_company(self):
        self.save()

    def delete_company(self):
        self.delete()
