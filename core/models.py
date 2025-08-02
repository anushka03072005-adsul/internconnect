from django.db import models

class Applicant(models.Model):
    ROLE_CHOICES = [
        ('intern', 'Intern'),
        ('volunteer', 'Volunteer')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    skills = models.TextField()

    def __str__(self):
        return self.name
