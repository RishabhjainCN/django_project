
from django.urls import path
from .views import *
urlpatterns = [
    path('user/',users,name = 'user'),
    path('project/',projects,name = 'proj'),
    path('project_user/',project_users,name = 'assignproj'),
    path('project_mentor/',project_mentor,name = 'assignproj'),
    path('mentees/<int:user_id>/',mentees,name = 'getmentees'),
    path('user_projects/<int:user_id>/',user_projects,name = 'getprojs'),
    path('project_users_mentors/<int:proj_id>/',project_users_mentors,name = 'getusers')
]
