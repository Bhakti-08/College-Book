'''from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    return render(request,'index.html')

def test_subjects(request):
    subject = models.TestSubject.objects.all()
    return render(request, 'test-subject.html',{'data':subject})'''