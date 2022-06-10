

from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("<b>Welome to Python + Django Class</b>")


def homepage(request):
    data = {'title' : 'My Home Page',
            'bdata' : 'This is a nice python and django session',
            'clist' : ['php','java','django'],
            'numbers' : [0,10,20,30,40,50],
            'stundents' : [
                {'name' : 'John' , 'phone' : 987468954885},
                {'name' : 'Jonathan' , 'phone' : 98647747747}
                ]
    }
    return render(request , "index2.html",data)


def courses(request):
    return HttpResponse("This is course page")


def coursesDetails(request,courseid):
    return HttpResponse(courseid)