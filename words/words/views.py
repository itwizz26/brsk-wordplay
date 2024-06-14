from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import re

def home (request):
    return render(request, 'index.html')

@csrf_protect
def read (request, *args, **kwargs):
    if request.method == 'POST':
        sentence = request.POST['sentence']
        result = scrabble(sentence)
        return HttpResponse(result)

def scrabble(sentence):
    try:
        scrabbled = ''
        words = open('./templates/words.txt')
        for word in re.findall(r'\w+', sentence):
            for needle in words:
                if (len(word.strip()) == len(needle.strip())) and (word[0] == needle[0]):
                    scrabbled += needle + ' '
                else:
                    scrabbled += word + ' '
                    break
        return scrabbled.strip()
    except:
       return "There was an error opening the file!"
