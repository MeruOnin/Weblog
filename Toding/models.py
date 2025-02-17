from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    # related
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_toDoList')
    # data
    task = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    fav = models.BooleanField(default=False)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reg_date']
        indexes = [
            models.Index(fields=['-reg_date'])
        ]

    def __str__(self):
        return self.task


class Users(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    # data
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    # choices
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )

    def __str__(self):
        return self.name