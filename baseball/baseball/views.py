# project1/baseball/views.py

from roster.models import Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


#home page for UNC athletics
def home (request):
    context = {'player_count': Player.objects.count()}
    return render(request, "roster/home.html", context)



