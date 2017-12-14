"""
Auto-generated class for Task
"""
from .Eco import Eco
from .EnumTaskState import EnumTaskState
from six import string_types

from . import client_support


class Task(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type action_name: str
        :type args: dict
        :type created: int
        :type eco: Eco
        :type guid: str
        :type service_guid: str
        :type service_name: str
        :type state: EnumTaskState
        :type template_name: str
        :rtype: Task
        """

        return Task(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Task'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.action_name = client_support.set_property('action_name', data, data_types, False, [], False, True, class_name)
        data_types = [dict]
        self.args = client_support.set_property('args', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.created = client_support.set_property('created', data, data_types, False, [], False, True, class_name)
        data_types = [Eco]
        self.eco = client_support.set_property('eco', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.guid = client_support.set_property('guid', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.service_guid = client_support.set_property('service_guid', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.service_name = client_support.set_property('service_name', data, data_types, False, [], False, True, class_name)
        data_types = [EnumTaskState]
        self.state = client_support.set_property('state', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.template_name = client_support.set_property('template_name', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)