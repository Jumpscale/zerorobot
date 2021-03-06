# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for BlueprintResult
"""
from .ServiceCreated import ServiceCreated
from .Task import Task

from . import client_support


class BlueprintResult(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type services: list[ServiceCreated]
        :type tasks: list[Task]
        :rtype: BlueprintResult
        """

        return BlueprintResult(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'BlueprintResult'
        data = json or kwargs

        # set attributes
        data_types = [ServiceCreated]
        self.services = client_support.set_property('services', data, data_types, False, [], True, True, class_name)
        data_types = [Task]
        self.tasks = client_support.set_property('tasks', data, data_types, False, [], True, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
