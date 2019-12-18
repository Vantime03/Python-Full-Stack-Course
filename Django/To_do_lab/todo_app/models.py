from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    completed_at = models.DateTimeField(blank = True, null = True)
    task_duration = models.DateTimeField(blank = True, null = True)

    TODO_TYPE = (
        ('p', 'personal'),
        ('f', 'family'),
        ('h', 'house'),
        ('m', 'misc'),
        ('s', 'school'),
    )

    todo_type = models.CharField(max_length=1, choices=TODO_TYPE, blank= True, default='m')

    def __str__(self):
            return self.title

    class Meta:
        ordering = ['title', 'created_at']