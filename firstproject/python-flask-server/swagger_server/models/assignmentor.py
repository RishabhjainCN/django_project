# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Assignmentor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mentorid: int=None, projid: int=None):  # noqa: E501
        """Assignmentor - a model defined in Swagger

        :param mentorid: The mentorid of this Assignmentor.  # noqa: E501
        :type mentorid: int
        :param projid: The projid of this Assignmentor.  # noqa: E501
        :type projid: int
        """
        self.swagger_types = {
            'mentorid': int,
            'projid': int
        }

        self.attribute_map = {
            'mentorid': 'mentorid',
            'projid': 'projid'
        }

        self._mentorid = mentorid
        self._projid = projid

    @classmethod
    def from_dict(cls, dikt) -> 'Assignmentor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The assignmentor of this Assignmentor.  # noqa: E501
        :rtype: Assignmentor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mentorid(self) -> int:
        """Gets the mentorid of this Assignmentor.


        :return: The mentorid of this Assignmentor.
        :rtype: int
        """
        return self._mentorid

    @mentorid.setter
    def mentorid(self, mentorid: int):
        """Sets the mentorid of this Assignmentor.


        :param mentorid: The mentorid of this Assignmentor.
        :type mentorid: int
        """

        self._mentorid = mentorid

    @property
    def projid(self) -> int:
        """Gets the projid of this Assignmentor.


        :return: The projid of this Assignmentor.
        :rtype: int
        """
        return self._projid

    @projid.setter
    def projid(self, projid: int):
        """Sets the projid of this Assignmentor.


        :param projid: The projid of this Assignmentor.
        :type projid: int
        """

        self._projid = projid
