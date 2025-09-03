from django.db import models

class Todo(models.Model):
    # title
    title = models.CharField(max_length=255)
    # description
    description = models.TextField()  
    # completed
    completed = models.BooleanField(default=False)
    # date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'TodoApp - {self.title}'
