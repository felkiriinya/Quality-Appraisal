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
    avg_rating = models.DecimalField(decimal_places=2, max_digits=3)
    avg_mentorship = models.DecimalField(decimal_places=2, max_digits=3)
    avg_hiring = models.DecimalField(decimal_places=2, max_digits=3)
    avg_community = models.DecimalField(decimal_places=2, max_digits=3)
    avg_corporate_dev = models.DecimalField(decimal_places=2, max_digits=3)
    avg_fundraising = models.DecimalField(decimal_places=2, max_digits=3)

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


    @property
    def avg_rating(self):
        quantity = Review.objects.filter(subject=self)
        overall_result = Review.objects.filter(subject=self).aggregate(avg_rating=Avg('overall'))['avg_rating']
        return overall_result if len(quantity) > 0 else float(0)
    
    @property
    def avg_mentorship(self):
        quantity = Review.objects.filter(subject=self)
        mentorship_result = Review.objects.filter(subject=self).aggregate(avg_mentorship=Avg('mentorship'))['avg_mentorship']
        return mentorship_result if len(quantity) > 0 else float(0)
    
    @property
    def avg_hiring(self):
        quantity = Review.objects.filter(subject=self)
        hiring_result = Review.objects.filter(subject=self).aggregate(avg_hiring=Avg('hiring'))['avg_hiring']
        return hiring_result if len(quantity) > 0 else float(0)
    
    @property
    def avg_community(self):
        quantity = Review.objects.filter(subject=self)
        community_result = Review.objects.filter(subject=self).aggregate(avg_community=Avg('community'))['avg_community']
        return community_result if len(quantity) > 0 else float(0)
    
    @property
    def avg_fundraising(self):
        quantity = Review.objects.filter(subject=self)
        fundraising_result = Review.objects.filter(subject=self).aggregate(avg_fundraising=Avg('fundraising'))['avg_fundraising']
        return fundraising_result if len(quantity) > 0 else float(0)
    
    @property
    def avg_corporate(self):
        quantity = Review.objects.filter(subject=self)
        corporate_result = Review.objects.filter(subject=self).aggregate(avg_corporate=Avg('corporate_development'))['avg_corporate']
        return corporate_result if len(quantity) > 0 else float(0)
     

class Review(models.Model):
    
    RATINGS=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = False)
    feedback = models.TextField(blank=False)
    title = models.CharField(max_length=200, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    mentorship = models.IntegerField(choices=RATINGS, blank=False, default=1)
    hiring = models.IntegerField(choices=RATINGS, blank=False, default=1)
    community = models.IntegerField(choices=RATINGS, blank=False, default=1)
    fundraising = models.IntegerField(choices=RATINGS, blank=False, default=1)
    corporate_development= models.IntegerField(choices=RATINGS, blank=False, default=1)
    overall = models.DecimalField(decimal_places=2, max_digits=3)


    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.overall = (int(self.mentorship) + int(self.hiring) + int(self.community) + \
            int(self.fundraising) + int(self.corporate_development)) / 5
        super(Review, self).save(*args, **kwargs)