"""Views for this Django app"""

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Movies
import json

def index(request):
    """Gets and displays all movies from the database on the index page"""

    movies = Movies.objects.all().order_by('-id')
    return render(request, 'index.html', {'movies': movies})

def movie(request, movie_name):
    """Show profile for a specific movie based on title"""

    title = movie_name.replace('_', ' ')
    movie = Movies.objects.get(title=title)
    return render(request, 'movie.html', {'movie': movie})

@csrf_exempt
def add_movie(request):
    """Adds a new movie to the database"""

    title = request.POST.get('title', '')
    year = request.POST.get('year', '')
    genre = request.POST.get('genre', '')

    new_movie = Movies(title=title, year=year, genre=genre)
    new_movie.save()

    # Generate New Record HTML; send back to Front-end
    new_record = Movies.objects.all().order_by('-id')[0]
    movie = {'id': new_record.id, 'title': new_record.title, 'year': new_record.year, 
             'genre': new_record.genre}
    new_record_HTML = render(request, 'new_row.html', {'movie': movie})

    # return as json 
    return HttpResponse(json.dumps({'result': 'Movie added!', 
                                    'html': str(new_record_HTML.content),
                                    'movie_id': new_record.id}))

def delete_movie(request, movie_id):
    """Deletes a movie from the database"""

    movie = Movies.objects.filter(id=movie_id)
    movie.delete()

    #return id for Front-end handling
    return HttpResponse(json.dumps({'result': 'ok', 'id': movie_id}))
