from django.db import models
import random as rnd
from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.db.models.signals import  pre_save
from django.dispatch import receiver

time_slots = (
    (1, 'an hour class'),
    (2, 'two hours class'),
    (3, 'three hours class'),
    
)

class Venue(models.Model):
    name = models.CharField(max_length=6)
    size = models.IntegerField(default=0)
    lab = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f' {self.name}'





class Course(models.Model):
    course_number = models.IntegerField(default=1,null=True, blank=True)
    course_name = models.CharField(max_length=40)



    def __str__(self):
        return f'{self.course_number} {self.course_name}'


class Department(models.Model):
    dept_id = models.IntegerField(null=True, blank=True)
    dept_name = models.CharField(max_length=50)
    size =models.IntegerField(default=1)

    @property
    def get_courses(self):
        return self.dept_name

    def __str__(self):
        return self.dept_name


class Section(models.Model):
    section_id = models.IntegerField(null=True,default=1)
    department = models.ManyToManyField(Department)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    time = models.IntegerField( default=1,choices=time_slots)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)
    lab = models.BooleanField(default=False)

@receiver(pre_save, sender=Instructor)
def slugify_title(sender, instance, *args, **kwargs):
    count = Instructor.objects.all().count()
    instance.number = count + 1

@receiver(pre_save, sender=Course)
def slugify_titl(sender, instance, *args, **kwargs):
    count = Course.objects.all().count()
    instance.course_number = count + 1


@receiver(pre_save, sender=Department)
def slugify_tit(sender, instance, *args, **kwargs):
    count = Department.objects.all().count()
    instance.dept_id = count + 1