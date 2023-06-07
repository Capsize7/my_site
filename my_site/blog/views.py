from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    repsonse = render_to_string('blog/index.html')
    return HttpResponse(repsonse)

def posts(request):
    return HttpResponse('Все посты блога')

def post_name(request, post):
    return HttpResponse(f'Информация о посте {post}')

def post_name_int(request, post_number):
    return HttpResponse(f'Здесь содержится информация о посте под номером {post_number}')