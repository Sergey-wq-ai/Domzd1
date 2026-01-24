import requests
from variables import TOKEN_NAME, PROJECT_ID


def test_change_id_name_project():
    headers = {
        'Authorization': TOKEN_NAME,
        'Content-Type': 'application/json'
    }

    body = {
        "deleted": False,
        "title": "новая-учеба2"
    }

    response = requests.put(
        f'https://ru.yougile.com/api-v2/projects/{PROJECT_ID}',
        headers=headers,
        json=body
    )
    print(response.json())