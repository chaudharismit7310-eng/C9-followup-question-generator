from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_normal_answer():
    res = client.post("/follow-up", json={"answer": "I used Redis for caching frequently accessed data."})
    assert "follow_up" in res.json()
    assert len(res.json()["follow_up"]) > 0

def test_short_answer():
    res = client.post("/follow-up", json={"answer": "Yes"})
    assert "more detail" in res.json()["follow_up"].lower()

def test_empty_answer():
    res = client.post("/follow-up", json={"answer": ""})
    assert "more detail" in res.json()["follow_up"].lower()

def test_off_topic_answer():
    res = client.post("/follow-up", json={"answer": "I like pizza and movies on weekends."})
    assert "follow_up" in res.json()

def test_technical_answer_specificity():
    res = client.post("/follow-up", json={"answer": "I used Redis for caching."})
    follow_up = res.json()["follow_up"].lower()
    assert "cache" in follow_up or "redis" in follow_up