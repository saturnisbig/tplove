from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def story(request):
    return render(request, 'story.html')

def photos(request):
    return render(request, 'photos.html')


def invitation(request):
    return render(request, 'invitation.html')


def zouguo(request):
    return render(request, 'zouguo.html')
