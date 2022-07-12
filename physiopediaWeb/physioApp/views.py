from re import template
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def displayStartup(request):
    template = loader.get_template('startupPage.html')
    return HttpResponse(template.render())

def displayLogin(request):
    template = loader.get_template('loginPage.html')
    return HttpResponse(template.render())

def displaySignUp(request):
    template = loader.get_template('signUpPage.html')
    return HttpResponse(template.render())

def displaySelection(request):
    template = loader.get_template('selection.html')
    return HttpResponse(template.render())

def displaySelectHeadNeckShoulder(request):
    template = loader.get_template('selectHeadNeckShoulder.html')
    return HttpResponse(template.render())

def displaySelectChestBackWaist(request):
    template = loader.get_template('selectChestBackWaist.html')
    return HttpResponse(template.render())

def displaySelectArmsHands(request):
    template = loader.get_template('selectArmsHands.html')
    return HttpResponse(template.render())

def displaySelectLegs(request):
    template = loader.get_template('selectLegs.html')
    return HttpResponse(template.render())

def displayMilestone(request):
    template = loader.get_template('currentMilestone.html')
    return HttpResponse(template.render())

def displayLog(request):
    template = loader.get_template('log.html')
    return HttpResponse(template.render())

def displaySettings(request):
    template = loader.get_template('profile-Setting.html')
    return HttpResponse(template.render())

def displayStore(request):
    template = loader.get_template('store.html')
    return HttpResponse(template.render())
