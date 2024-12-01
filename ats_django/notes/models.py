from django.db import models
from django.contrib.auth.models import User
from candidates.models import Candidate

class Note(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.user.username} for {self.candidate.name}"
