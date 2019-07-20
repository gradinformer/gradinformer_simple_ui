from .settings import yandex_geocoder_key
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'base.html')

def events(request):
	return render(request, 'event_list.html')

def event_history(request):
	return HttpResponse("Event history")

def event_add(request):
	context = {"yandex_geocoder_key": yandex_geocoder_key}
	return render(request, 'add.html', context)

def registration(request):
	return render(request, 'registration.html')

def auth(request):
	return render(request, 'auth.html')

def event(request, event_id):
	return HttpResponse("Event")

def event_change(request, event_id):
	return HttpResponse("Change event")

