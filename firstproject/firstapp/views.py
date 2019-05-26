from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from rest_framework.decorators import api_view

from .models import project_user, person, project

def errorhandling(func):
	def func_wrapper(*args, **kwargs):
		try:
			return func(*args,**kwargs)
		except Exception as ex:
			return HttpResponse(ex)
	return func_wrapper

@csrf_exempt
@require_http_methods("POST")
@errorhandling
def users(request):
    json_data = json.loads(request.body.decode('utf-8'))
    instance = person(name = json_data.get('name' + ""))
    instance.save()
    return HttpResponse(status = '200')

@csrf_exempt
@require_http_methods("POST")
@errorhandling
def projects(request):
    json_data = json.loads(request.body.decode('utf-8'))
    instance = project(name = json_data.get('name')+"")
    instance.save()
    return HttpResponse(status = '200')

@csrf_exempt
@require_http_methods("POST")
@errorhandling
def project_users(request):
    json_data = json.loads(request.body.decode('utf-8'))
    for user_id in json_data['users']:
        instance = project_user(p_id = project.objects.get(id = json_data['proj']+0) , u_id = person.objects.get(id = user_id+0), is_mentor = False)
        instance.save()
    return HttpResponse(status = '200')

@csrf_exempt
@require_http_methods("POST")
@errorhandling
def project_mentor(request):
    json_data = json.loads(request.body.decode('utf-8'))
    instance = project_user(p_id = project.objects.get(id = json_data['projid']+0), u_id = person.objects.get(id = json_data['mentorid']+0), is_mentor = True)
    instance.save()
    return HttpResponse(status = '200')

@csrf_exempt
@require_http_methods("GET")
@errorhandling
def mentees(request,user_id):
    projects_id = project_user.objects.filter(u_id = user_id+0, is_mentor = True).values_list('p_id',flat = True)
    mentees_id = project_user.objects.filter(p_id__in = projects_id,is_mentor = False).values_list('u_id',flat = True)
    return_data = {'result' : list(person.objects.filter(id__in = mentees_id).values_list())}
    return HttpResponse(json.dumps(return_data), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
@errorhandling
def user_projects(request,user_id):
    proj_ids = list(project_user.objects.filter(u_id = user_id+0).values_list('p_id',flat = True))
    return_data = {'results' : list(project.objects.filter(id__in = proj_ids).values_list())}
    return HttpResponse(json.dumps(return_data), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
@errorhandling
def project_users_mentors(request,proj_id):
    users_ids = list(project_user.objects.filter(p_id = proj_id+0, is_mentor = False).values_list('u_id',flat = True))
    mentors_ids = list(project_user.objects.filter(p_id = proj_id, is_mentor = True).values_list('u_id',flat = True))
    return_data = {}
    return_data['users'] = list(person.objects.filter(id__in = users_ids).values_list())
    return_data['mentors'] = list(person.objects.filter(id__in = mentors_ids).values_list())
    return HttpResponse(json.dumps(return_data), content_type='text/json')

