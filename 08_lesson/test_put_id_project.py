import os
import uuid
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

class TestPutProject:
    """Тесты для обновления проекта"""
    
    @pytest.fixture
    def project_id(self):
        """Создаем проект для тестов"""
        api_key = os.getenv("YOUGILE_API_KEY")
        if not api_key:
            pytest.skip("API ключ не найден")
        
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=headers,
            json={"title": f"Тест {uuid.uuid4().hex[:6]}"}
        )
        
        if response.status_code != 201:
            pytest.skip(f"Не удалось создать проект: {response.status_code}")
        
        return response.json()["id"]
    
    def test_update_project_success(self, project_id):
        """✅ ПОЗИТИВНЫЙ: обновление проекта"""
        api_key = os.getenv("YOUGILE_API_KEY")
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        new_title = f"Обновлено {uuid.uuid4().hex[:6]}"
        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{project_id}",
            headers=headers,
            json={"title": new_title}
        )
        
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        print(f"✅ Проект обновлен: {new_title}")
    
    def test_update_project_no_auth(self, project_id):
        """❌ НЕГАТИВНЫЙ: обновление без авторизации"""
        headers = {"Content-Type": "application/json"}  
        
        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{project_id}",
            headers=headers,
            json={"title": "Без токена"}
        )
        
        assert response.status_code in [401, 403], f"Ожидалась ошибка 401/403, получен {response.status_code}"
        print("✅ API защищено: без токена нельзя")

if __name__ == "__main__":
    
    load_dotenv()
    api_key = os.getenv("YOUGILE_API_KEY")
    
    if not api_key:
        print("❌ API ключ не найден")
        exit(1)
    
    print("=== Тестирование PUT /projects/{id} ===\n")
    
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    create_resp = requests.post(
        "https://ru.yougile.com/api-v2/projects",
        headers=headers,
        json={"title": f"Тест {uuid.uuid4().hex[:6]}"}
    )
    
    if create_resp.status_code != 201:
        print(f"❌ Не удалось создать проект: {create_resp.status_code}")
        exit(1)
    
    project_id = create_resp.json()["id"]
    print(f"✅ Проект создан: {project_id}")
    
    
    print("\n1. 🟢 Позитивный тест...")
    new_title = f"Обновлено {uuid.uuid4().hex[:6]}"
    update_resp = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        headers=headers,
        json={"title": new_title}
    )
    
    if update_resp.status_code == 200:
        print(f"   ✅ Успех! Новое название: {new_title}")
    else:
        print(f"   ❌ Ошибка: {update_resp.status_code}")
    
    
    print("\n2. 🔴 Негативный тест...")
    bad_headers = {"Content-Type": "application/json"}
    bad_resp = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        headers=bad_headers,
        json={"title": "Без токена"}
    )
    
    if bad_resp.status_code in [401, 403]:
        print(f"   ✅ Успех! API вернул ошибку: {bad_resp.status_code}")
    else:
        print(f"   ❌ Ошибка: ожидалась 401/403, получен {bad_resp.status_code}")
    
    print(f"\n📝 ID проекта для очистки: {project_id}")