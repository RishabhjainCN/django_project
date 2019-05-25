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
    instance = person(name = json_data.get('name')+"")
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
    user_id = person.objects.get(id = user_id+0)
    proj_users_id = project_user.objects.filter(u_id = user_id, is_mentor = True).values_list('id',flat = True)
    projects_id = set({})
    for proj_user in proj_users_id:
        projects_id.add(project_user.objects.get(id=proj_user).p_id)
    mentors_id = []
    for project_id in projects_id:
        mentors_id += project_user.objects.filter(p_id = project_id, is_mentor = False).values_list('u_id',flat = True)
    mentors_name_id = []
    for mentor_id in mentors_id:
        mentors_name_id.append((person.objects.get(id=mentor_id).name, mentor_id))
    return_data = {}
    return_data['result'] = mentors_name_id
    return HttpResponse(json.dumps(return_data), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
@errorhandling
def user_projects(request,user_id):
    user = person.objects.get(id=user_id+0)
    proj_users = project_user.objects.filter(u_id=user, is_mentor=True).values_list('id', flat=True)
    projects_name_id = []
    for proj_user in proj_users:
        projects_name_id.append((project_user.objects.get(id = proj_user).p_id.name,project_user.objects.get(id = proj_user).p_id.id))
    return_data = {}
    return_data['results'] = projects_name_id
    return HttpResponse(json.dumps(return_data), content_type = 'text/json')

@csrf_exempt
@require_http_methods("GET")
@errorhandling
def project_users_mentors(request,proj_id):
    proj = project.objects.get(id=proj_id+0)
    proj_users = project_user.objects.filter(p_id=proj, is_mentor = False).values_list('id', flat=True)
    users_name_id = []
    for proj_user in proj_users:
        users_name_id.append((project_user.objects.get(id = proj_user).u_id.name,project_user.objects.get(id = proj_user).u_id.id))
    proj_users = project_user.objects.filter(p_id=proj, is_mentor=True).values_list('id', flat=True)
    mentors_name_id = []
    for proj_user in proj_users:
        mentors_name_id.append((project_user.objects.get(id=proj_user).u_id.name,project_user.objects.get(id=proj_user).u_id.id))

    return_data = {}
    return_data['users'] = users_name_id
    return_data['mentors'] = mentors_name_id
    return HttpResponse(json.dumps(return_data), content_type='text/json')

