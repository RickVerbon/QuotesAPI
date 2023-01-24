from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Quote(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_body = models.TextField()
    context = models.CharField(max_length=30)
    source = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_author
