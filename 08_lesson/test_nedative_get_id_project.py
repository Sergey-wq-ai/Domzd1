import requests
from variables import TOKEN_NAME, PROJECT_ID


def test_get_id_project():
    headers = {
        'Authorization': TOKEN_NAME,
        'Content-Type': 'application/json'
    }

    response = requests.get(
        f'https://ru.yougile.com/api-v2/projects/{PROJECT_ID}',
        headers=headers
    )
    print(response.json())