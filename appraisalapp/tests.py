from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company,Review

# Create your tests here.
     

class CompanyTestClass(TestCase):
    def setUp(self):
        self.felista=User(username = 'Felista', email='felkiriinuya@gmail.com', password='iloveme')
        self.company= Company(name= 'Felistabuisness', website='felista.com', locations='africa', sector_focus='all', duration='1year',deal='1000000KES',bio='amazing',logo='fel.jpg', user = self.felista)
        self.felista.save()
        self.company.save()

    def tearDown(self):
        # Company.objects.all.delete()
        # User.objects.all.delete()
        pass

    def test_instance(self):
        self.assertTrue(isinstance(self.felista, User))
        self.assertTrue(isinstance(self.company, Company))        
         


class ReviewTestClass(TestCase):
    def setUp(self):
        
        self.felista=User(username = 'Felista', email='felkiriinuya@gmail.com', password='iloveme')
        self.company= Company(name= 'Felistabuisness', website='felista.com', locations='africa', sector_focus='all', duration='1year',deal='1000000KES',bio='amazing',logo='fel.jpg', user = self.felista)
        self.review = Review(company = self.company, user = self.felista, feedback='Amazing',title='feedback', mentorship=3, hiring=4, community=5, fundraising=2, corporate_development=1)
        self.felista.save()
        self.company.save()
        self.review.save()

    def tearDown(self):
       
        # User.objects.all().delete()
        # Company.objects.all().delete()   
        # Review.objects.all().delete() 
        pass

    
    def test_review_instance(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_save_review(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_review(self):
        review1 = Review.objects.all()
        self.assertEqual(len(review1),1)

        self.review.delete_review()

        review2 = Review.objects.all()
        self.assertEqual(len(review2),0)      