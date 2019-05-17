import random
import django_rq

from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def _digest(item, number):
    item.process_time = number
    print(f'add new item ({number})')
    item.save()

def enqueue(request, number):
    item = Item()
    django_rq.enqueue(_digest, item, number)
    return HttpResponse(f'enqueue item with process time {number}')
    
def list(request):
    query_set = Item.objects.all()
    print_set = set(str(item) for item in query_set)
    print(print_set)
    return HttpResponse(f'list of items: {print_set}')
     

