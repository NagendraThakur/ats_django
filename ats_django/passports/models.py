from django.db import models
from candidates.models import Candidate

class Passport(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='passports'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=50)
    expiry_date = models.DateField()
    issuing_country = models.CharField(max_length=100)
    passport_file = models.FileField(upload_to='passports/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport_number}"
