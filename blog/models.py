from django.db import models

# Create your models here.

class Blog(models.Model):
    # author = 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}'

