# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assignmentor import Assignmentor  # noqa: E501
from swagger_server.models.assignproj import Assignproj  # noqa: E501
from swagger_server.models.proj import Proj  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_firstapp_mentees_user_id_get(self):
        """Test case for firstapp_mentees_user_id_get

        get mentees of a given mentor
        """
        response = self.client.open(
            '/firstapp/mentees/{user_id}/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_project_mentor_post(self):
        """Test case for firstapp_project_mentor_post

        assign mentor to a project
        """
        mentorid_and_projectid = Assignmentor()
        response = self.client.open(
            '/firstapp/project_mentor/',
            method='POST',
            data=json.dumps(mentorid_and_projectid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_project_post(self):
        """Test case for firstapp_project_post

        create new project
        """
        project = Proj()
        response = self.client.open(
            '/firstapp/project/',
            method='POST',
            data=json.dumps(project),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_project_user_post(self):
        """Test case for firstapp_project_user_post

        assign project to users
        """
        projectid_and_usersid = Assignproj()
        response = self.client.open(
            '/firstapp/project_user/',
            method='POST',
            data=json.dumps(projectid_and_usersid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_project_users_mentors_proj_id_get(self):
        """Test case for firstapp_project_users_mentors_proj_id_get

        get users and mentors of given project
        """
        response = self.client.open(
            '/firstapp/project_users_mentors/{proj_id}/'.format(proj_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_user_post(self):
        """Test case for firstapp_user_post

        create new user
        """
        name = User()
        response = self.client.open(
            '/firstapp/user/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_user_projects_user_id_get(self):
        """Test case for firstapp_user_projects_user_id_get

        get projects of given user
        """
        response = self.client.open(
            '/firstapp/user_projects/{user_id}/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
