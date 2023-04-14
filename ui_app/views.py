import os
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import speech_recognition  as sr

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def english_view(request):
    if request.method == 'POST':
        r = sr.Recognizer()
        print("Please start speaking...")
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio, language="en-US")
            print(text)
            return JsonResponse({'text': text})
        
    return render(request, 'english.html')

def french_view(request):
    return render(request, 'french.html')

def spanish_view(request):
    return render(request, 'spanish.html')
