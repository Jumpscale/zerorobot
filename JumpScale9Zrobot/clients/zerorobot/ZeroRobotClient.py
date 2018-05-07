import time

from js9 import j

from .client import Client

JSConfigClientBase = j.tools.configmanager.base_class_config


_template = """
url = "http://localhost:6600"
jwt_ = ""
secrets_ = []
"""


class ZeroRobotClient(JSConfigClientBase):

    def __init__(self, instance="main", data={}, parent=None, template=None, ui=None, interactive=True):
        """
        @param instance: instance name
        @param data: configuration data. if specified will update the configuration with it
        @param parent: used by configmanager, you probably don't need to deal with it manually
        """
        data = data or {}
        super().__init__(instance=instance, data=data, parent=parent, template=_template, ui=ui, interactive=interactive)
        self._api = None
        self._jwt_expire_timestamp = None

    @property
    def api(self):
        """
        regroup all of the method to talk to the ZeroRobot API
        """
        jwt = self.config.data.get('jwt_')
        if jwt and not self._jwt_expire_timestamp:
            try:
                self._jwt_expire_timestamp = j.clients.itsyouonline.jwt_expire_timestamp(jwt)
            except KeyError:
                # case when jwt does not have expiration time
                pass

        if self._jwt_expire_timestamp and self._jwt_expire_timestamp - 300 < time.time():
            jwt = j.clients.itsyouonline.refresh_jwt_token(jwt, validity=3600)
            self._jwt_expire_timestamp = j.clients.itsyouonline.jwt_expire_timestamp(jwt)
            self.config.data_set('jwt_', jwt)
            self.config.save()
            self._api = None

        if self._api is None:
            self._api = Client(base_uri=self.config.data["url"])
            if self.config.data.get('jwt_'):
                header = 'Bearer %s' % self.config.data['jwt_']
                self._api.security_schemes.passthrough_client_iyo.set_authorization_header(header)
            if self.config.data.get('secrets_'):
                header = 'Bearer %s' % ' '.join(self.config.data['secrets_'])
                self._api.security_schemes.passthrough_client_zrobot.set_zrobot_header(header)
        return self._api