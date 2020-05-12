from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from Two.models import User





def get_user(request):
    username = "jia"
    password = "abc"

    users = User.objects.filter(u_name=username)

    if users.exists():
        user = users.first()

        if user.u_password == password:
            print ("ok")
        else:
            print ("no")
    else:
        print("不存在")
    return HttpResponse("ok")


def get_usera(request):
    jia = User.objects.all()[1:3]

    context = {
        "name": jia
    }

    return render(request,"jia.html",context=context)
