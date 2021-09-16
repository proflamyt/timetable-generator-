from django.forms import ModelForm
from. models import *
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Venue
        fields = [
            'name',
            'size',
            'lab'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = [
            
            'name'
        ]





class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'size']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'course','time','instructor', 'lab']
