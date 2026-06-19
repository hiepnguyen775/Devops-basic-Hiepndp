"""Unit test tầng API — MOCK DB nên KHÔNG cần Postgres thật (nhanh, chạy trong CI).

Chạy:  cd solutions/backend && pip install -r requirements.txt && pytest -v

Mẹo: KHÔNG dùng `with TestClient(app)` để tránh chạy lifespan (init_db gọi DB thật).
Tạo client thường → lifespan startup không chạy → test độc lập hạ tầng.
"""
from fastapi.testclient import TestClient
from app import main, db

client = TestClient(main.app)


def test_health_khong_can_db():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_notes_yeu_cau_dang_nhap():
    # Chưa có token -> 401
    r = client.get("/api/notes")
    assert r.status_code == 401


def test_validate_title_rong_tra_422():
    # Override auth để bỏ qua xác thực, tập trung test validation
    main.app.dependency_overrides[main.get_current_user] = lambda: {"id": 1, "username": "test"}
    r = client.post("/api/notes", json={"title": "", "content": "x"})
    assert r.status_code == 422   # title min_length=1
    main.app.dependency_overrides.clear()


def test_tao_va_liet_ke_note(monkeypatch):
    main.app.dependency_overrides[main.get_current_user] = lambda: {"id": 1, "username": "test"}
    fake = {"id": 1, "title": "Hello", "content": "world", "created_at": "2026-01-01T00:00:00Z"}
    monkeypatch.setattr(db, "create_note", lambda uid, t, c: fake)
    monkeypatch.setattr(db, "list_notes", lambda uid: [fake])

    r = client.post("/api/notes", json={"title": "Hello", "content": "world"})
    assert r.status_code == 201
    assert r.json()["title"] == "Hello"

    r2 = client.get("/api/notes")
    assert r2.status_code == 200
    assert len(r2.json()) == 1

    main.app.dependency_overrides.clear()


def test_xoa_note_khong_ton_tai_tra_404(monkeypatch):
    main.app.dependency_overrides[main.get_current_user] = lambda: {"id": 1, "username": "test"}
    monkeypatch.setattr(db, "delete_note", lambda uid, nid: False)  # giả lập không tìm thấy

    r = client.delete("/api/notes/999")
    assert r.status_code == 404

    main.app.dependency_overrides.clear()
