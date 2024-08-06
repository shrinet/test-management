def test_create_test(client, token):
    response = client.post(
        "/tests/",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Sample Test"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Sample Test"

def test_create_question(client, token):
    response = client.post(
        "/questions/",
        headers={"Authorization": f"Bearer {token}"},
        json={"test_id": 1, "text": "Sample Question"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Sample Question"
