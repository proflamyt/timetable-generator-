from django.shortcuts import redirect, render
from .models import *
from .forms import *
import json
from sys import path
path.append('/home/olamide/Documents/genetic algorithm/mujeeb/olamide')
from pathlib import Path
from olamide import  Ngra
from olamide import HtmlOutput
from olamide import Configuration
from pathlib import Path
import time
from django.shortcuts import render




js = []
olam = []
def home(request):
    return render(request, 'index.html', {})


def timetable(request):
    venue = Venue.objects.all()
    for i in venue.values():
        ola = {'venue': i} 
        js.append(ola)
    instructor  =  Instructor.objects.all()
    for i in instructor.values():
        ola = {'prof': i}
        js.append(ola)
    course  =  Course.objects.all()
    for i in course.values():
        ol ={'course': i}
        js.append(ol)
    department  = Department.objects.all()
    for i in department.values():
        p ={'group': i}
        js.append(p)
    section  =  Section.objects.all()
    ola = section.count()
    for i,j in zip(section.values(), range(ola)):
        olam = []
        for j in section[j].department.values():
            olam.append(j["id"])
            
        i["group"]=olam
        h ={'class': i}
        js.append(h)
    ola = json.dumps(js, indent=4)
    print(ola)
    with open('olamide/mujeeb.json', 'w') as olam:
        olam.write(ola)

    file_name = "/olamide/mujeeb.json"
    start_time = int(round(time.time() * 1000))

    configuration = Configuration.Configuration()  
    target_file = str(Path().absolute()) + file_name
    print(target_file)
    configuration.parseFile(target_file)
    alg = Ngra.Ngra(configuration)
    alg.run()
    html_result = HtmlOutput.HtmlOutput.getResult(alg.result)
    return render(request, html_result)


def add_instructor(request):
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addinstructor')
    context = {
        'form': form
    }
    return render(request, 'adins.html', context)


def inst_list_view(request):
    context = {
        'instructors': Instructor.objects.all()
    }
    return render(request, 'instlist.html', context)


def delete_instructor(request, pk):
    inst = Instructor.objects.filter(pk=pk)
    if request.method == 'POST':
        inst.delete()
        return redirect('editinstructor')


def add_room(request):
    form = RoomForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addroom')
    context = {
        'form': form
    }
    return render(request, 'addrm.html', context)


def room_list(request):
    context = {
        'rooms': Room.objects.all()
    }
    return render(request, 'rmlist.html', context)


def delete_room(request, pk):
    rm = Room.objects.filter(pk=pk)
    if request.method == 'POST':
        rm.delete()
        return redirect('editrooms')


def meeting_list_view(request):
    context = {
        'meeting_times': MeetingTime.objects.all()
    }
    return render(request, 'mtlist.html', context)


def add_meeting_time(request):
    form = MeetingTimeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addmeetingtime')
        else:
            print('Invalid')
    context = {
        'form': form
    }
    return render(request, 'addmt.html', context)


def delete_meeting_time(request, pk):
    mt = MeetingTime.objects.filter(pk=pk)
    if request.method == 'POST':
        mt.delete()
        return redirect('editmeetingtime')


def course_list_view(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'crslist.html', context)


def add_course(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addcourse')
        else:
            print('Invalid')
    context = {
        'form': form
    }
    return render(request, 'adcrs.html', context)


def delete_course(request, pk):
    crs = Course.objects.filter(pk=pk)
    if request.method == 'POST':
        crs.delete()
        return redirect('editcourse')


def add_department(request):
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('adddepartment')
    context = {
        'form': form
    }
    return render(request, 'addep.html', context)


def department_list(request):
    context = {
        'departments': Department.objects.all()
    }
    return render(request, 'deptlist.html', context)


def delete_department(request, pk):
    dept = Department.objects.filter(pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('editdepartment')


def add_section(request):
    form = SectionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('addsection')
    context = {
        'form': form
    }
    return render(request, 'addsec.html', context)


def section_list(request):
    context = {
        'sections': Section.objects.all()
    }
    return render(request, 'seclist.html', context)


def delete_section(request, pk):
    sec = Section.objects.filter(pk=pk)
    if request.method == 'POST':
        sec.delete()
        return redirect('editsection')
