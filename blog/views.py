from django.shortcuts import render

# Create your views here.
from django.db import models
 
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

from django.shortcuts import render_to_response
 
from blog.models import posts
 
def home(request):
    return render_to_response('index.html')
