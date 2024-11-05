from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    status = models.BooleanField(default=False)  # True - done, False - not done

    def __str__(self):
        return self.task
    

