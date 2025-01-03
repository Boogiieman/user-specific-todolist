from django.db import models

class Task(models.Model):
    list = models.TextField()
    status = models.BooleanField(default= False)

    def __str__(self):
        return f"{self.list} : {self.status}"
