from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Games
from .forms import GamesForm

def home(request):
    # Your view logic here
    home = "Welcome to the NFL Season Tracker"
    
    return render(request, 'home.html', {'home': home})

def games_interface(request):
    if request.method == 'POST':
        if 'game_id' in request.POST:
            # Handle editing a game
            game_id = request.POST['game_id']
            game = Games.objects.get(game_id=game_id)
            form = GamesForm(request.POST, instance=game)
            if form.is_valid():
                form.save()
        else:
            # Handle adding a new game
            form = GamesForm(request.POST)
            if form.is_valid():
                form.save()

    form = GamesForm()
    games = Games.objects.all()
    
    return render(request, 'games_interface.html', {'form': form, 'games': games})

def edit_game(request, temp_game_id):
    game = get_object_or_404(Games, game_id=temp_game_id)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games_interface')
    else:
        form = GamesForm(instance=game)
    
    games = Games.objects.all()
    
    return render(request, 'games_interface.html', {'form': form, 'games': games})

def delete_game(request, game_id):
    game = Games.objects.get(game_id=game_id)
    game.delete()
    return HttpResponseRedirect(reverse('games_interface'))

def report_interface(request):    
    if request.method == 'POST':
        year = request.POST.get('year')
        week_number = request.POST.get('week_number')
        
        if year:
            # Filter games by year
            games = Games.objects.filter(date_played__year=year)
            
            if week_number:
                # Filter further by week number
                games = games.filter(week_number=week_number)
        else:
            games = Games.objects.all()

        return render(request, 'report_interface.html', {'games': games})
    else:
        games = Games.objects.all()
        return render(request, 'report_interface.html', {'games': games})