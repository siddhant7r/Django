from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)

def __str__(self):
    return f"{self.stu_name} ({self.stu_email})"
