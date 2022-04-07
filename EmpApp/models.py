
from django.db import models

class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Salary=models.IntegerField()
    Emp_ID=models.IntegerField()
    Image=models.ImageField(upload_to="images/")
    Resume=models.FileField(upload_to="resumes/")

    def __str__(self):
        return self.Name
