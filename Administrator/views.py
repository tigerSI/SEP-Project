from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse


def dashboard(request):
    context = {'name' : "Atichat"}
    return render(request, 'Administrator/index.html', context)
