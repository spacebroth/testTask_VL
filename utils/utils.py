import json


def print_response(response):
    text = response.text

    if text and text != '404 page not found':
        try:
            parsed_response = json.loads(text)
            formatted_res = json.dumps(parsed_response, ensure_ascii=False, indent=2)
        except json.JSONDecodeError:
            formatted_res = text
    else:
        formatted_res = response.content
    if formatted_res:
        return formatted_res.replace("'", "''")
