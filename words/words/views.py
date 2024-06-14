from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request, 'index.html')

def read (request, *args, **kwargs):
    if request.method == 'POST':
        sentence = request.POST['sentence']
        result = scrabble(sentence)
        return HttpResponse(result)
    
def scrabble(sentence):
    try:
        with open('words.txt') as file:
            print(sentence)
            print(file.read);
    except:
        print("There was an error opening the file!")
