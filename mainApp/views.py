from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def homeTest(requst):
    return HttpResponse('hello')