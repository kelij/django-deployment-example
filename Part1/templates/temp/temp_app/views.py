from django.shortcuts import render

# Create your views here.

def index(request):
    cr_dict =  {'insert_me' : 'Hello I am from  temp_app/views.py !'}
    return render(request, 'index.html' ,context = cr_dict)
