import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    news_task_data = {"title": "Nova tarefa", "description": "Descrição"}

    response = requests.post(f"{BASE_URL}/tasks", json=news_task_data)

    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task_by_id():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]
