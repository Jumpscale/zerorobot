"""
This module expose the high level API that is meant to be used by service developer in the template actions.

It provie ways to create and list services from a group of ZeroRobots in a unified way.
"""

from js9 import j

from zerorobot import service_collection as scol
from zerorobot import template_collection as tcol
from zerorobot.dsl.ZeroRobotManager import ZeroRobotManager


class TemplateNotFoundError(Exception):
    """
    This exception is raised when trying to create a service
    from a template that doesn't exists
    """
    pass


class ServicesMgr:

    def __init__(self, base):
        self._base = base

    @property
    def names(self):
        """
        Return a dictionnary that contains all the service present on all
        the accessible ZeroRobots

        key is the name of the service
        value is a Service or ServiceProxy object
        """
        services = scol._name_index
        for robot in self._base.robots.values():
            services.update(robot.services.names)
        return services

    @property
    def guids(self):
        """
        Return a dictionnary that contains all the service present on all
        the accessible ZeroRobot

        key is the guid of the service
        value is a Service or ServiceProxy object
        """
        services = scol._guid_index
        for robot in self._base.robots.values():
            services.update(robot.services.guids)
        return services

    def create(self, template_uid, service_name, data=None):
        """
        Instantiate a service from a template
        This method first look for a ZeroRobot that manages the template_uid then create the service in the selected robots.

        If this methos is used from a service action, it first check if we can create the service in the local robot.
        If not, it looks for a remote robot to create the service onto.

        @param template_uid: UID of the template to use a base class for the service
        @param service_name: name of the service, needs to be unique within the robot instance
        @param data: a dictionnary with the data of the service to create
        @return: A Service or ServiceProxy object. depending if the service has been created locally or remotely
        """
        try:
            # we can create a service locally, the local robot has the template
            template = tcol.get(template_uid)
            return tcol.instantiate_service(template, service_name, data)
        except KeyError:
            # we need to look for a robot that handle this template
            pass

        try:
            # try to find a robot that manage the template with uid template_uid
            robot = self._base.get_robot(template_uid)
        except KeyError:
            raise TemplateNotFoundError("no robot managing the template %s found" % template_uid)

        return robot.services.create(template_uid, service_name, data)


class ZeroRobotAPI:
    # TODO: find better name

    def __init__(self):
        self._config_mgr = ConfigMgr()
        self.services = ServicesMgr(self)

    @property
    def robots(self):
        """
        list all the ZeroRobot accessible
        return a dictionary with
        key = url of the API of the robot
        value: ZeroRobotClient object
        """
        robots = {}
        for instance in self._config_mgr.list():
            robots[instance] = ZeroRobotManager(instance)
        return robots

    def get_robot(self, template_uid):
        """
        returns a instance of ZeroRobotClient that is managing the template identified by template_uid

        It looks into all the know ZeroRobots which one manages the template_uid and return a client to it.
        If not known robots managed the template_uid, then KeyError is raised
        """
        for robot in self.robots.values():
            if template_uid in robot.templates.uids:
                return robot
        raise KeyError("no robot that managed %s found" % template_uid)


class ConfigMgr():
    """
    Small class that abstract configmanager
    """

    location = 'j.clients.zrobot'

    def __init__(self):
        j.tools.configmanager.interactive = False

    def list(self):
        """
        list all the available zerorobot client configured

        @return: a list of instance name
        """
        return j.tools.configmanager.list(self.location)

    def set(self, instance, base_url):
        """
        create a new config

        @param instance: instance name
        @param base_url: base_url of the client
        """
        config = {'url': base_url}
        cfg = j.tools.configmanager.js9_obj_get(self.location, instance, data=config).config
        # make sure it exists on disk
        cfg.save()
        return cfg

    def delete(self, instance):
        """
        deletes a config
        @param instance: instance name
        """
        if instance not in self.list():
            return
        j.clients.zrobot.delete(instance)