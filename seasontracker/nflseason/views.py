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
    years = list(range(1920, 2024))  # Years from 1920 to 2023
    weeks = list(range(1, 24))       # Weeks from 1 to 23
    
    if request.method == 'POST':
        # Retrieve the selected filters (year and week) from the form
        selected_year = request.POST.get('year')
        selected_week = request.POST.get('week')
        
        # Query the Games table based on the selected filters
        filtered_games = Games.objects.filter(year=selected_year, week_number=selected_week)
        
        return render(request, 'report_interface.html', {'years': years, 'weeks': weeks, 'filtered_games': filtered_games})
    
    return render(request, 'report_interface.html', {'years': years, 'weeks': weeks, 'filtered_games': None})