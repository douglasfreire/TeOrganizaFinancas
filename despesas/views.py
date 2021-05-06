from django.shortcuts import render
from django.http import HttpResponse


def despesastest(request):
    return HttpResponse('despesas')
