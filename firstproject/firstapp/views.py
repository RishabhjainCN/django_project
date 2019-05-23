from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

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
    instance = project(name = jsondata.get('n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ame'))
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
def getmentees(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    user = person.objects.get(id = jsondata['user'])
    projuser = projectuser.objects.filter(u_id = user, is_mentor = True).values_list('id',flat = True)
    mentors = []
    for pu in projuser:
        if projectuser.objects.get(id = pu).is_mentor == False:
            mentors.append(projectuser.objects.get(id = pu).u_id.name)
    returndata = {}
    returndata['result'] = mentors
    return HttpResponse(json.dumps(returndata), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
def getprojs(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    user = person.objects.get(id=jsondata['user'])
    projuser = projectuser.objects.filter(u_id=user, is_mentor=True).values_list('id', flat=True)
    projects = []
    for i in projuser:
        projects.append(projectuser.objects.get(id = i).p_id.name)
    returndata = {}
    returndata['results'] = projects
    return HttpResponse(json.dumps(returndata), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
def getusers(request):
    jsondata = json.loads(request.body.decode('utf-8'))
    proj = project.objects.get(id=jsondata['proj'])
    projuser = projectuser.objects.filter(p_id=proj, is_mentor = False).values_list('id', flat=True)
    users = []
    for i in projuser:
        users.append(projectuser.objects.get(id = i).u_id.name)
    mentors = []
    projuser = projectuser.objects.filter(p_id=proj, is_mentor=True).values_list('id', flat=True)
    mentors = []
    for i in projuser:
        mentors.append(projectuser.objects.get(id=i).u_id.name)

    returndata = {}
    returndata['users'] = users
    returndata['mentors'] = mentors
    return HttpResponse(json.dumps(returndata), content_type='text/json')

