from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the waste_controller index.")

def detail(request, sensor_id):
    return HttpResponse(f"You're looking at sensor{sensor_id}.")