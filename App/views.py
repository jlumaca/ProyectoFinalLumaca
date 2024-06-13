from django.shortcuts import render

# Create your views here.

def inicio(req):
    return render(req,"index.html",{})

