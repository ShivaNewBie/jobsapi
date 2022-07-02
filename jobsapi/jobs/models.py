from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=250)
    company_email = models.EmailField(max_length=250)
    job_title = models.CharField(max_length=250) 
    job_description = models.TextField(max_length=250)
    salary = models.IntegerField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name}"