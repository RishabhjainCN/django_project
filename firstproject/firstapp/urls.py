
from django.urls import path
from .views import *
urlpatterns = [
    path('user/',createuser,name = 'user'),
    path('proj/',createproj,name = 'proj'),
    path('assignproj/',assignproj,name = 'assignproj'),
    path('assignmentor/',assignmentor,name = 'assignproj'),
    path('getmentees/<int:userid>/',getmentees,name = 'getmentees'),
    path('getprojs/<int:userid>/',getprojs,name = 'getprojs'),
    path('getusers/<int:projid>/',getusers,name = 'getusers')
]
