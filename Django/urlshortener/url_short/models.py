from django.db import models

class Todo(models.Model):
    code = models.CharField(max_length=6)
    url = models.TextField(max_length=300)

    def __str__(self):
            return self.url

    class Meta:
        ordering = ['id', 'url']