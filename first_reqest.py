import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Статус:", response.status_code)
print("Тело:", response.json())

def test_et_post_returns_200():
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

data = response.json();

assert response.status_code == 200
assert data["id"] == 1
assert data["userId"] == 1
assert isinstance(data["title"], str) and len(data["title"]) > 0
assert isinstance(data["body"], str) and len(data["body"]) > 0

print("Все гуд")
