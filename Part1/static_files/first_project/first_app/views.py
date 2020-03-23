from django.shortcuts import render

# Create your views here.
def index(request):
    my_dic = {'insert_me' : 'This is from views.py'}
    return render(request, 'index.html', context=my_dic)
