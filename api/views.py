import json
from mujeeb.timetable.models import Course, Department, Instructor, Section, Venue
js = []
olam = []
def home(request):
    venue = Venue.objects.all()
    for i in venue.values():
        ola = {'venue': i} 
        js.append(ola)
    instructor  =  Instructor.objects.all()
    for i in instructor.values():
        ola = {'instructor': i}
        js.append(ola)
    course  =  Course.objects.all()
    for i in course.values():
        ol ={'course': i}
        js.append(ol)
    department  = Department.objects.all()
    for i in department.values():
        p ={'department': i}
        js.append(p)
    section  =  Section.objects.all()
 
    for i in section.values():
        for j in section:
            o = j.department.all()
            for p in o:
                print(o)
                if p not in olam: 
                    olam.append(p.id)
            i["group"]=olam
        h ={'section': i}
        js.append(h)
    ola = json.dumps(js, indent=4)
    with open('mujeeb.json') as file:
        file.write(ola)
    return 'ok'

    #add blog
home()