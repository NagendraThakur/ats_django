from django.db import models
# from passports.models import Passport

class Candidate(models.Model):
    STATUS_CHOICES = [
        ('NEW_LEAD', 'New Lead'),
        ('REACHED_OUT', 'Reached Out'),
        ('RESPONDED', 'Responded'),
        ('NEW_APPLICATION', 'New Application'),
        ('RECRUITER_SCREEN', 'Recruiter Screen'),
        ('FIRST_INTERVIEW', '1st Interview'),
        ('SECOND_INTERVIEW', '2nd Interview'),
        ('REFERENCE_CHECK', 'Reference Check'),
        ('OFFER', 'Offer'),
        ('BACKGROUND_CHECK', 'Background Check'),
        ('HIRED', 'Hired'),
        ('REJECTED', 'Rejected'),
        ('BAND', 'Band'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW_LEAD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # passport = models.OneToOneField(
    #     Passport, 
    #     on_delete=models.SET_NULL,  # Sets to NULL if the linked passport is deleted
    #     null=True, 
    #     blank=True
    # )

    def __str__(self):
        return self.name
