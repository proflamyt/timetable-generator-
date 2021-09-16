from mujeeb.timetable.models import *

section  =  Section.objects.all()
olamid  =  section.values()
for j,z in zip(section,section.count()):
    o = j.department.all()
    for p in o:
        olamid[z] = p
                 

        
        

for j in section.values():
    olam = []
    for i in olamid:
        i[i]

        i["group"]=i
        h ={'class': i}