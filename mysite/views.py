from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from mysite.models import Profile


def index(request):
    context = User.objects.all()
    return render(request, 'index.html', {'context': context})


def index_detail(request, pk):
    context = Profile.objects.get(pk=pk)
    return render(request, 'index_detail.html', {'context': context})

