#python -m http.server 9000

from django.shortcuts import render,redirect
import webbrowser


import os
def nikhila(request):
    os.system('python -m http.server 9000')
    webbrowser.open('http://localhost:9000')
    return render(request,"welcome.html")
