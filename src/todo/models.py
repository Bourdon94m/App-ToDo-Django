from django.db import models

# Create your models here.


class Task_ToDo(models.Model):
    title = models.CharField(max_length=50, blank=False)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Task"


    def __str__(self) -> str:
        return self.title