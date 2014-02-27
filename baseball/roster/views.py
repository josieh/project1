# project1/baseball/roster/views.py
from roster.models import Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


#home page for UNC athletics on bigger app - this will actually be teams 

def home (request): 
    return render(request, 'roster/home.html', {"player": player})
    #return render(request, "roster/home.html") - this is without importing players... doesn't matter they
    #won't be show up anyway

    

#list page 
def roster (request):
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 25)
    page = request.GET.get('page')
    try:
        players=paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(1)
    return render(request, "roster/player_list.html", {'player': player})


#detail page 
def player (request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/detail.html", {'player': player})

