# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
from .Action import Action
from .Error import Error
from .Logs import Logs
from .Service import Service
from .ServiceCreated import ServiceCreated
from .Task import Task
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class ServicesService:
    def __init__(self, client):
        self.client = client

    def ListActions(self, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        List all the possible action a service can do.
        It is method for GET /services/{service_guid}/actions
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/actions"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Action(elem))
                return resps, resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def GetLogs(self, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        returns the logs of the services tasks
        It is method for GET /services/{service_guid}/logs
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/logs"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return Logs(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def CancelTask(self, task_guid, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Cancel a task
        It is method for DELETE /services/{service_guid}/task_list/{task_guid}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/task_list/" + task_guid
        return self.client.delete(uri, None, headers, query_params, content_type)

    def GetTask(self, task_guid, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Retrieve the detail of a task
        It is method for GET /services/{service_guid}/task_list/{task_guid}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/task_list/" + task_guid
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return Task(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def getTaskList(self, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Return all the action in the task list
        It is method for GET /services/{service_guid}/task_list
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/task_list"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Task(elem))
                return resps, resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def AddTaskToList(self, data, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Add a task to the task list
        It is method for POST /services/{service_guid}/task_list
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid + "/task_list"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return Task(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def DeleteService(self, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a service
        It is method for DELETE /services/{service_guid}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid
        return self.client.delete(uri, None, headers, query_params, content_type)

    def GetService(self, service_guid, headers=None, query_params=None, content_type="application/json"):
        """
        Get the detail of a service
        It is method for GET /services/{service_guid}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services/" + service_guid
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return Service(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def listServices(self, headers=None, query_params=None, content_type="application/json"):
        """
        List all the services known by the ZeroRobot.
        It is method for GET /services
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(Service(elem))
                return resps, resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def createService(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        create a new service
        It is method for POST /services
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/services"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return ServiceCreated(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
