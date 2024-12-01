from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    TARGET_TYPE_CHOICES = [
        ('candidate', 'Candidate'),
        ('job', 'Job'),
        ('application', 'Application'),
        ('interview', 'Interview'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    target_type = models.CharField(max_length=20, choices=TARGET_TYPE_CHOICES)
    target_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"
