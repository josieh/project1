# project1/baseball/roster/views.py
from roster.models import Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


#home page for UNC athletics on bigger app


#list page 
def roster (request):
    player = Player.objects.order.by(number)[0],
    return render(request, "roster/list.html", {'player': player})

#detail page 
def player (request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/detail.html", {'player': player})