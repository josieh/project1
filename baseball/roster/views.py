# project1/baseball/roster/views.py
from roster.models import Coach, Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


#home page for UNC athletics on bigger app - this will actually be teams 

def home (request):
    context= {
        'message' : " ",
        'player_count': Player.objects.count()
    }
    return render(request, 'roster/home.html', context)
    
    #return render(request, "roster/home.html") - this is without importing players... doesn't matter they
    #won't be show up anyway

    

#list page 
def roster (request):
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 100)
    page = request.GET.get('page')
    try:
        players=paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(1)
    return render(request, "roster/player_list.html", {'players': players})
    
    


#detail page 
def player (request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/detail.html", {'player': player})
    


    
def coach(request,pk):
	coach = get_object_or_404(Coach, id=pk)
	return render(request, "roster/coach.html", {"coach":coach})

def coachList(request):
	coach_list = Coach.objects.all()
	paginator = Paginator(coach_list, 100)
	page = request.GET.get('page')
	try:
		coaches=paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		coaches=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		coaches = paginator.page(paginator.num_pages)

	return render(request, 'roster/coach_list.html', {"coaches":coaches})

