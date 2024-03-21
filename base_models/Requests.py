import logging
import requests
from utils.allure.attachment import attach_request_and_response_body, attach_curl
from utils.utils import print_response


class Requests:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def getRequest(url, path, params={}, headers={}, kwargs={}):
        response = requests.get(f"{url}{path}", headers=headers, params=params, **kwargs)

        Requests.LOGGER.info(
            f'\nGET {url}{path} with \nparams {params},\nkwargs {kwargs},\nheaders {headers}\n'
            f'--- Response: {print_response(response)}')

        attach_request_and_response_body(response)
        attach_curl(response)
        return response

    @staticmethod
    def postRequest(url, path, data={}, json={}, params={}, headers={}, kwargs={}):
        response = requests.post(f'{url}{path}', data=data, json=json,
                                 headers=headers, params=params, **kwargs)

        Requests.LOGGER.info(
            f'\nPOST {url}{path} with\nparams {params},\ndata {data},\njson {json},\nkwargs {kwargs},\nheaders {headers}\n'
            f'--- Response: {print_response(response)}')

        attach_request_and_response_body(response)
        attach_curl(response)
        return response
