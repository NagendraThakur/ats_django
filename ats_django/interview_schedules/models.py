from django.db import models
from candidates.models import Candidate
from jobs.models import Job
from django.contrib.auth.models import User

class InterviewSchedule(models.Model):
    MODE_CHOICES = [
        ('online', 'Online'),
        ('in-person', 'In Person'),
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='interviews')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='interviews')
    scheduled_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_interviews')
    date_time = models.DateTimeField()
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview for {self.candidate.name} - {self.job.title}"
