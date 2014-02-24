# project1/baseball/roster/views.py

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home (request):
    context = {'message': 'This is a dynamic message variable!'}
    return render(request, "base.html")


    
