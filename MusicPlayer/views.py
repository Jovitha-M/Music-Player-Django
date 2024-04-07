from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from MusicPlayer.models import Song, WatchLater
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginpage(request):
  if(request.method == 'POST'):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = uname, password = password)
    if user is not None:
      login(request, user)
      return redirect('Home')
    else:
      return HttpResponse("Invalid Credentials")
  return render(request, "MusicPlayer/login.html")

def logoutuser(request):
  logout(request)
  return redirect('Login')

def register(request):
  if(request.method == 'POST'):
    uname = request.POST.get('username')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('confirm_password')

    if(pass1 != pass2):
      messages.error(request, "Password not same")
      return redirect('Register')
    else:
      user = User.objects.create_user(uname,email,pass1)
      user.save()
    return redirect('Login')
  return render(request, "MusicPlayer/register.html")


def add_to_watch_later(request, song_id):
    if request.method == 'POST':
        user = request.user  
        song = Song.objects.get(pk=song_id)
        if(WatchLater.objects.filter(user=user, song=song).exists()):
            return redirect('watchlater')
        watch = WatchLater.objects.create(user=user, song=song)
        print(watch)
    return redirect('watchlater') 

def watch_later_list(request):
    user = request.user
    watch_later_songs = WatchLater.objects.filter(user=user)  # Optimize query with select_related
    context = {'watch_later_songs': watch_later_songs}
    return render(request, 'MusicPlayer/watch_later.html')

def sample(request):
  return render(request, "MusicPlayer/sample.html")

from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth.models import User
from MusicPlayer.models import Song, WatchLater

def home(request):
    songs = Song.objects.all()
    search_query = request.GET.get('query', '')
    if request.user.is_authenticated:
        user = request.user  # Get the authenticated user instance
        watch_later_songs = WatchLater.objects.filter(user=user)
    else:
        user = None
        watch_later_songs = []

    watch_later_list = [watch_later.song for watch_later in watch_later_songs]

    if search_query:
        songs = songs.filter(title__icontains=search_query)

    context = {'songs': songs, 'search_query': search_query, 'current_year': date.today().year}
    return render(request, 'MusicPlayer/home.html', context)


def about(request):
  return render(request, 'MusicPlayer/about.html')