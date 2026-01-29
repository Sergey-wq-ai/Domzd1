import pytest
import requests
import os
import time
from dotenv import load_dotenv


load_dotenv()

def test_get_project_positive():
    """Позитивный тест получения проекта"""
    
    
    api_key = os.getenv('YOUGILE_API_KEY')
    base_url = 'https://ru.yougile.com/api-v2'
    
    if not api_key:
        pytest.skip("API ключ не найден. Создайте файл .env с YOUGILE_API_KEY=ваш_ключ")
    
   
    headers = {
        'Authorization': f'Bearer {api_key}',  
        'Content-Type': 'application/json'
    }
    
    
    project_data = {"title": f"Тестовый проект {int(time.time())}"}
    
    create_response = requests.post(
        f"{base_url}/projects",
        json=project_data,
        headers=headers
    )
    
    assert create_response.status_code == 201, "Не удалось создать проект"
    
   
    project_id = create_response.json()["id"]
    print(f"📝 Создан тестовый проект ID: {project_id[:8]}...")
    
    try:
        
        get_response = requests.get(
            f"{base_url}/projects/{project_id}",
            headers=headers
        )
        
        
        assert get_response.status_code == 200, "Ошибка получения проекта"
        
        data = get_response.json()
        assert data["id"] == project_id, "ID не совпадает"
        assert "title" in data, "Нет названия проекта"
        assert isinstance(data["title"], str), "Название не строка"
        
        print(f"✅ Проект получен: {data['title']}")
        
    finally:
        
        try:
            requests.delete(f"{base_url}/projects/{project_id}", headers=headers)
            print(f"🧹 Тестовый проект удален")
        except Exception as e:
            print(f"⚠️  Не удалось удалить проект (возможно API не поддерживает): {e}")

def test_get_project_negative():
    """Негативный тест получения несуществующего проекта"""
    
    
    api_key = os.getenv('YOUGILE_API_KEY')
    base_url = 'https://ru.yougile.com/api-v2'
    
    if not api_key:
        pytest.skip("API ключ не найден. Создайте файл .env с YOUGILE_API_KEY=ваш_ключ")
    
    headers = {
        'Authorization': f'Bearer {api_key}',  
        'Content-Type': 'application/json'
    }
    
    
    fake_id = "00000000-0000-0000-0000-000000000000"
    
    response = requests.get(
        f"{base_url}/projects/{fake_id}",
        headers=headers
    )
    
    
    assert response.status_code in [404, 400], f"Ожидалась ошибка 404/400, получен {response.status_code}"
    
    print(f"✅ Негативный тест пройден: API вернул {response.status_code}")