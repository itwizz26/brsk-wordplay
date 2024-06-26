# Brsk Word Play (BWP)

BWP is a Python v3 and Django v5 attempt at solving the below problem.

## The Problem

We have an eccentric Scrabble playing client who sometimes requests us to write software that can help them train for their Scrabble matches, and the client has a new request.

This time around, they would like to be able to run a specific program, that given a sentence, will replace each word in the sentence with another word starting with the same letter that is the same length. If a particular word can’t be found that matches the criteria above, then the original word should be returned. Another requirement is that the same input should return a different output each time. Said another way, the word that is picked should be any random word that fulfills the criteria.

### Examples

Given the sentence lightly fried fish are delicious, the program may return likable frier frog arm delegated. Running it again may yield lenient fuses foam any digressed.

### Resources we are using
The client trains for his Scrabble matches using the 370000 word list here: https://github.com/dwyl/english-words/blob/master/words_alpha.txt. The solution should therefore use this same word list to generate the new sentences.

### How to run the app

To clone all the files locally from GitHub and run the Django server, run these commdands from the terminal:

```
git clone https://github.com/itwizz26/brsk-wordplay.git
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Now change into words/ and run this command to start the server:
```
./manage.py runserver (or python3 manage.py runserver)
```
Open the frontend in your browser from:
``
http://localhost:8000/
``

## License
MIT &copy; 2024 Daniel Mathebula
