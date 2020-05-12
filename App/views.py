import random


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        jia = random.randrange(100)
        person.p_name = "jia%d" % i
        person.p_age = jia
        person.p_sex = jia % 2
        person.save()
    return HttpResponse("批量创建成功")

def get_persons(request):
    persons = Person.objects.filter(p_age__gt=50).filter(p_age__lt=80)
    context = {
        "persons": persons
    }


    return render(request,"person_list.html",context=context)

def get_exclude(request):
    #persons = Person.objects.exclude(p_age__gt=50).exclude(p_age__lt=20)

   # persons_tow = Person.objects.filter(p_age__in=[40,26,28])
    persons_tow = Person.objects.all().order_by("p_age")
    context={
        "persons": persons_tow
    }
    return render(request,"person_list.html",context=context)

def add_person(request):
    persons = Person.objects.create(p_name="加害人3")
    persons.save()
    return HttpResponse('ok')


