from django.http import HttpResponse, JsonResponse
import json


def index(request):  #star2
    return HttpResponse("Welcome to colors app")

color_list = ['blue', 'red', 'green']


def list(request):  #star2/list
    return HttpResponse(json.dumps(color_list), content_type="application/json")


def add(request): #star2/add?name=yellow
    color = request.GET.get('name')
    if color in color_list:
        response_data = {'message': 'color {} is already in the list'.format(color)}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=409)
    elif color is None:
        return HttpResponse('Please add a color')
    else:
        color_list.append(color)
        return HttpResponse(json.dumps(color_list), content_type="application/json", status=201)


def get(request):
    color = request.GET.get('name')
    if color not in color_list:
        response_data = {'message': 'color does not exist'}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)
    return HttpResponse(color)

