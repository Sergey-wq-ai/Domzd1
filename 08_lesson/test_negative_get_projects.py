import requests
from variables import TOKEN_NAME


def test_get_project():
    headers = {
        'Authorization': TOKEN_NAME,
        'Content-Type': 'application/json'
    }

    response = requests.get(
        'https://ru.yougile.com/api-v2/projects',
        headers=headers
    )
    print(response.json())