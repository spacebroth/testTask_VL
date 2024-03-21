import json
import allure
import curlify
from requests import Response


def attach_request_and_response_body(response: Response):
    if response.text == '':
        allure.attach('No Response body', 'Response', allure.attachment_type.TEXT)
    else:
        allure.attach(
            f'URL: {response.request.url}\n\nHeaders: {response.request.headers}\n\nBody: {response.request.body}',
            'Request', allure.attachment_type.JSON)
        allure.attach(f'{response.headers}\n\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}',
                      'Response', allure.attachment_type.JSON)


def attach_curl(response: Response):
    curl_command = curlify.to_curl(response.request)
    allure.attach(f'{curl_command}', 'cURL', allure.attachment_type.TEXT)
