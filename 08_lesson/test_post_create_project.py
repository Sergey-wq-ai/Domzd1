import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_API_KEY")

def test_create_project_success():
    """✅ ПОЗИТИВНЫЙ ТЕСТ: создание проекта с токеном"""
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    project_name = f"Тест {uuid.uuid4().hex[:6]}"
    payload = {"title": project_name}
    
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json=payload
    )
    
    
    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
    
    data = response.json()
    assert "id" in data, "В ответе нет поля 'id'"
    
    print(f"✅ Проект создан: {data['id']}")
    
   
    os.environ["LAST_CREATED_PROJECT_ID"] = data["id"]

def test_create_project_no_auth():
    """❌ НЕГАТИВНЫЙ ТЕСТ: создание без токена"""
    headers = {"Content-Type": "application/json"}
    payload = {"title": "Проект без токена"}
    
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json=payload
    )
    
    
    assert response.status_code in [401, 403], f"Ожидалась ошибка 401/403, получен {response.status_code}"
    print("✅ API защищено: запрос без токена отклонен")

if __name__ == "__main__":
    print("=== Тестирование YouGile API ===\n")
    
    
    if not TOKEN:
        print("❌ Токен не найден. Создайте .env файл с YOUGILE_API_KEY=ваш_токен")
        exit(1)
    
    print(f"🔑 Токен найден ({len(TOKEN)} символов)\n")
    
    
    print("1. 🟢 Позитивный тест...")
    try:
        test_create_project_success()
        print(f"   ✅ Успех!\n")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}\n")
    
     
    print("2. 🔴 Негативный тест...")
    try:
        test_create_project_no_auth()
        print(f"   ✅ Успех!\n")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}\n")
    
    print("=== Тестирование завершено ===")