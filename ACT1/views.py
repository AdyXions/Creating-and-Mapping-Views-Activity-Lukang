from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def mission(request):
    title = "Mission"
    content = "The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence."
    return render(request, "ccms.html", {'type':title, 'content':content})
def vision(request):
    title = "Vision"
    content = "The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education."
    return render(request, "ccms.html", {'type':title, 'content':content})
def objective(request):
    title = "Objective"
    content = "3"
    return render(request, "ccms.html", {'type':title, 'content':content})

