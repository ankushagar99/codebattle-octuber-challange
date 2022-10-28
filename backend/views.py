from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from backend.serializers import AdvocateSerializer
from .models import Advocate


# Create your views here.

@api_view(['GET'])
def all_routes(request):
    routes = ['advocates', 'adovates/:username']
    return Response(routes)

@api_view(['GET']) 
def all_advocates(request):
    query = request.GET.get('query')
    if query == None:
        advocates = Advocate.objects.all()
    else:
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query) | Q(name__icontains=query))

    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_advocate(request, username):
    advocates = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocates, many=False)
    return Response(serializer.data)
