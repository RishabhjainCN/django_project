from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from rest_framework.decorators import api_view

from .models import projectuser, person, project

@csrf_exempt
@require_http_methods("POST")
def createuser(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    instance = person(name = jsondata.get('name'))
    instance.save()
    return HttpResponse(status = '201')

@csrf_exempt
@require_http_methods("POST")
def createproj(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    instance = project(name = jsondata.get('name'))
    instance.save()
    return HttpResponse(status = '201')

@csrf_exempt
@require_http_methods("POST")
def assignproj(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    for userid in jsondata['users']:
        instance = projectuser(p_id = project.objects.get(id = jsondata['proj']), u_id = person.objects.get(id = userid), is_mentor = False)
        instance.save()
    return HttpResponse(status = 201)

@csrf_exempt
@require_http_methods("POST")
def assignmentor(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    instance = projectuser(p_id = project.objects.get(id = jsondata['projid']), u_id = person.objects.get(id = jsondata['mentorid']), is_mentor = True)
    instance.save()
    return HttpResponse(status = 201)

@csrf_exempt
@require_http_methods("GET")
def getmentees(request,userid):
    user = person.objects.get(id = userid)
    projuser = projectuser.objects.filter(u_id = user, is_mentor = True).values_list('id',flat = True)
    projects = set({})
    for pu in projuser:
        projects.add(projectuser.objects.get(id=pu).p_id)
    mentors = []
    for p in projects:
        mentors += projectuser.objects.filter(p_id = p, is_mentor = False).values_list('u_id',flat = True)
    _mentors = []
    for i in mentors:
        _mentors.append(person.objects.get(id=i).name)
    returndata = {}
    returndata['result'] = _mentors
    return HttpResponse(json.dumps(returndata), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
def getprojs(request,userid):
    user = person.objects.get(id=userid)
    projuser = projectuser.objects.filter(u_id=user, is_mentor=True).values_list('id', flat=True)
    projects = []
    for i in projuser:
        projects.append(projectuser.objects.get(id = i).p_id.name)
    returndata = {}
    returndata['results'] = projects
    return HttpResponse(json.dumps(returndata), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
def getusers(request,projid):
    proj = project.objects.get(id=projid)
    projuser = projectuser.objects.filter(p_id=proj, is_mentor = False).values_list('id', flat=True)
    users = []
    for i in projuser:
        users.append(projectuser.objects.get(id = i).u_id.name)
    projuser = projectuser.objects.filter(p_id=proj, is_mentor=True).values_list('id', flat=True)
    mentors = []
    for i in projuser:
        mentors.append(projectuser.objects.get(id=i).u_id.name)

    returndata = {}
    returndata['users'] = users
    returndata['mentors'] = mentors
    return HttpResponse(json.dumps(returndata), content_type='text/json')

