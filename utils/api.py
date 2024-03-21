from base_models.Requests import Requests


class TestAPI:
    def __init__(self, base_url):
        self._api_base_url = base_url
        self.headers = {'accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json'}

    def _send_get(self, path, params={}, headers={}, kwargs={}):
        headers.update(self.headers)
        return Requests.getRequest(url=self._api_base_url, path=path, params=params, headers=headers, kwargs=kwargs)

    def _send_post(self, path, json={}, headers={}, params={}, kwargs={}):
        headers.update(self.headers)
        return Requests.postRequest(url=self._api_base_url, path=path, json=json, params=params, headers=headers,
                                    kwargs=kwargs)

    def object(self):
        from endpoints.obj_api import ObjApi
        return ObjApi(self._api_base_url)

    def version(self):
        from endpoints.version import VersionApi
        return VersionApi(self._api_base_url)
