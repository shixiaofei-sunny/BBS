from django.shortcuts import render

# Create your views here.


def list(request):

    data = {}
    return render(request,'list.html',data)

def read(request):
    data = {}
    return render(request,'read.html',data)

