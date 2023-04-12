import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def english_view(request):
    if request.method == 'POST':
        audio_file = request.FILES['recorded_audio']
        fs = FileSystemStorage()
        print("Loading")
        filename = fs.save(audio_file.name, audio_file)
        file_url = fs.url(filename)
    return render(request, 'english.html')

def french_view(request):
    return render(request, 'french.html')

def spanish_view(request):
    return render(request, 'spanish.html')
