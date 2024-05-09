from django.db import models

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    std_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.std_number}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course_code = models.CharField(max_length=10)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.student.name}'s grade in {self.course_code}: {self.value}"

