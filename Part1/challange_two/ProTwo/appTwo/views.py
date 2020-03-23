from django.shortcuts import render

# Create your views here.
def index(request):
    my_dc = {'help_insertion' : 'Help page'}
    return render(request,'help.html',context=my_dc)
