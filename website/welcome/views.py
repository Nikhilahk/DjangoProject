from django.shortcuts import render,redirect
from django.core.files import File
#from website.pythonscript import nikhila

import webbrowser
import os
#os.system('python -m http.server 9000')


def welcomeaction(request):
    webbrowser.open('http://localhost:8001')
    os.system('python -m http.server 8001')
    return render(request,'login_page.html')
# Create your views here.
