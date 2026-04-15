from django.db import models

# Create your models here.
class Feedback(models.Model):
    comments = models.TextField()
    image = models.ImageField(upload_to='feedback_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        Return f"Feedback {self.id} - {self.created_at}"