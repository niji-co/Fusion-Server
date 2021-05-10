from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

import datetime

class HeroViewSet(viewsets.ModelViewSet()):
   queryset = Hero.objects.all().order_by('name')
   serializer_class = HeroSerializer


# def hello(request):
#     text = """<h1>Welcome to my app!</h1>"""
#     return HttpResponse(text)

# def hello(request):
#     today = datetime.datetime.now().date()
#     return render(request, "hello.html", {"today" : today})

# def hello(request):
#    today = datetime.datetime.now().date()
   
#    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#    return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

# def viewArticle(request, articleID):
#     text = "Displaying article number : %s"%articleID
#     return HttpResponse(text)

# def viewArticles(request, month, year):
#     text = "Displaying articles of : %s/%s"%(year, month)
#     return HttpResponse(text)

# def crudops(request):
#    #Creating an entry
   
#    dreamreal = Dreamreal(
#       website = "www.polo.com", mail = "sorex@polo.com", 
#       name = "sorex", phonenumber = "002376970"
#    )
   
#    dreamreal.save()
   
#    #Read ALL entries
#    objects = Dreamreal.objects.all()
#    res ='Printing all Dreamreal entries in the DB : <br>'
   
#    for elt in objects:
#       res += elt.name+"<br>"
   
#    #Read a specific entry:
#    sorex = Dreamreal.objects.get(name = "sorex")
#    res += 'Printing One entry <br>'
#    res += sorex.name
   
#    #Delete an entry
#    res += '<br> Deleting an entry <br>'
#    sorex.delete()
   
#    #Update
#    dreamreal = Dreamreal(
#       website = "www.polo.com", mail = "sorex@polo.com", 
#       name = "sorex", phonenumber = "002376970"
#    )
   
#    dreamreal.save()
#    res += 'Updating entry<br>'
   
#    dreamreal = Dreamreal.objects.get(name = 'sorex')
#    dreamreal.name = 'thierry'
#    dreamreal.save()
   
#    return HttpResponse(res)