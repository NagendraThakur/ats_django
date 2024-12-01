from django.db import models
from candidates.models import Candidate
from jobs.models import Job

class Application(models.Model):
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('IN_REVIEW', 'In Review'),
        ('SHORTLISTED', 'Shortlisted'),
        ('OFFERED', 'Offered'),
        ('REJECTED', 'Rejected'),
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUBMITTED')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} - {self.job.title}"
