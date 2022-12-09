from django.shortcuts import render
from .models import Project
import mimetypes
import os
from django.http.response import HttpResponse

def home(request):
    projects = Project.objects
    return render(request, "projects/home.html", {'projects': projects})

def download(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Tanjim-Ahmed-Khan-Resume.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/media/docs/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
