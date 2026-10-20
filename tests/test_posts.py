import pytest


def test_get_post_returns_200(api_session):
    response = api_session.get(f"{api_session.base_url}/posts/1")
    assert response.status_code == 200


def test_post_has_expected_fields(api_session):
    response = api_session.get(f"{api_session.base_url}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_post_id_maches_requested(api_session):
    response = api_session.get(f"{api_session.base_url}/posts/1")
    data = response.json()
    assert data["id"] == 1

    
def test_get_nonexistend_post_returns_404(api_session):
    response = api_session.get(f"{api_session.base_url}/posts/99999")
    data = response.json()
    assert response.status_code == 404

@pytest.mark.parametrize("post_id", [1, 2, 3, 10, 100])
def test_posts_exist(api_session, post_id):
    response = api_session.get(f"{api_session.base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
