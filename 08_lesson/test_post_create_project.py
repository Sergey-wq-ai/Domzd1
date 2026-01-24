import requests
from variables import TOKEN_NAME


def test_create_project():
    headers = {
        'Authorization': TOKEN_NAME,
        'Content-Type': 'application/json'
    }

    body = {
        "title": "Учёба5"
    }

    response = requests.post(
        'https://ru.yougile.com/api-v2/projects',
        headers=headers,
        json=body
    )
    print(response.json())