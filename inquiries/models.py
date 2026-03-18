from django.db import models
from django.utils import timezone

class Inquiry(models.Model):
    PLAN_CHOICES = [
        ('Starter', 'Starter - ₹19,999/m'),
        ('Growth', 'Growth - ₹39,999/m'),
        ('Scale', 'Scale - ₹49,999/m'),
        ('Domination', 'Domination - ₹74,999/m'),
        ('Normal Website', 'Normal Website - ₹6,000'),
        ('E-commerce Website', 'E-commerce Website - ₹10,000'),
        ('Logo + Branding', 'Logo + Branding - ₹15,000-₹20,000'),
        ('Photography Only', 'Photography Only - ₹20,000'),
        ('Photo + Video Package', 'Photo + Video Package - ₹25,000-₹35,000'),
    ]
    
    inquiry_id = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=200, blank=True, null=True)
    selected_plan = models.CharField(max_length=100, choices=PLAN_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.inquiry_id:
            import random
            self.inquiry_id = f"GRV{random.randint(100000, 999999)}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.inquiry_id} - {self.name} - {self.selected_plan}"
