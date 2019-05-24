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

    def test_firstapp_assignmentor_post(self):
        """Test case for firstapp_assignmentor_post

        assign mentor to a project
        """
        mentorid_and_projectid = Assignmentor()
        response = self.client.open(
            '/firstapp/assignmentor/',
            method='POST',
            data=json.dumps(mentorid_and_projectid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_assignproj_post(self):
        """Test case for firstapp_assignproj_post

        assign project to users
        """
        projectid_and_usersid = Assignproj()
        response = self.client.open(
            '/firstapp/assignproj/',
            method='POST',
            data=json.dumps(projectid_and_usersid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_getmentees_userid_get(self):
        """Test case for firstapp_getmentees_userid_get

        get mentees of a given mentor
        """
        response = self.client.open(
            '/firstapp/getmentees/{userid}/'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_getprojs_userid_get(self):
        """Test case for firstapp_getprojs_userid_get

        get projects of given user
        """
        response = self.client.open(
            '/firstapp/getprojs/{userid}/'.format(userid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_getusers_projid_get(self):
        """Test case for firstapp_getusers_projid_get

        get users and mentors of given project
        """
        response = self.client.open(
            '/firstapp/getusers/{projid}/'.format(projid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_firstapp_proj_post(self):
        """Test case for firstapp_proj_post

        create new project
        """
        project = Proj()
        response = self.client.open(
            '/firstapp/proj/',
            method='POST',
            data=json.dumps(project),
            content_type='application/json')
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


if __name__ == '__main__':
    import unittest
    unittest.main()
