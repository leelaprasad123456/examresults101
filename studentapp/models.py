from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    maths = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percent = models.DecimalField(max_digits=5, decimal_places=2)

    def _str_(self):
        return self.name
