import connexion
import six

from swagger_server.models.assignmentor import Assignmentor  # noqa: E501
from swagger_server.models.assignproj import Assignproj  # noqa: E501
from swagger_server.models.proj import Proj  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def firstapp_assignmentor_post(mentorid_and_projectid=None):  # noqa: E501
    """assign mentor to a project

     # noqa: E501

    :param mentorid_and_projectid: this is ids of project and mentor
    :type mentorid_and_projectid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        mentorid_and_projectid = Assignmentor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def firstapp_assignproj_post(projectid_and_usersid=None):  # noqa: E501
    """assign project to users

     # noqa: E501

    :param projectid_and_usersid: this is ids of users to whom project has to be assigned
    :type projectid_and_usersid: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        projectid_and_usersid = Assignproj.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def firstapp_getmentees_userid_get(userid):  # noqa: E501
    """get mentees of a given mentor

     # noqa: E501

    :param userid: this is id of mentor whose mentees has to be printed
    :type userid: int

    :rtype: None
    """
    return 'do some magic!'


def firstapp_getprojs_userid_get(userid):  # noqa: E501
    """get projects of given user

     # noqa: E501

    :param userid: this is id of user whose project has to be displayed
    :type userid: int

    :rtype: None
    """
    return 'do some magic!'


def firstapp_getusers_projid_get(projid):  # noqa: E501
    """get users and mentors of given project

     # noqa: E501

    :param projid: this is id of project whose users and mentors has to be displayed
    :type projid: int

    :rtype: None
    """
    return 'do some magic!'


def firstapp_proj_post(project=None):  # noqa: E501
    """create new project

     # noqa: E501

    :param project: this is name of project created
    :type project: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project = Proj.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def firstapp_user_post(name=None):  # noqa: E501
    """create new user

     # noqa: E501

    :param name: this is name of user created
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
