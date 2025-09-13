from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello, World</h1>')

def home(request):
    mymembers = Member.objects.all().values()
    # template = loader.get_template('myfirst.html')
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))