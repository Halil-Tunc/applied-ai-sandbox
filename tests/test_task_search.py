"""Focused tests for note search on the homepage."""


def test_search_by_title(client, app):
    app.notes.clear()
    app.notes.extend([
        {"title": "Flask tutorial", "body": "Learn Flask"},
        {"title": "Shopping list", "body": "Milk and eggs"},
    ])
    r = client.get("/?q=Flask")
    assert b"Flask tutorial" in r.data
    assert b"Shopping list" not in r.data


def test_search_by_body(client, app):
    app.notes.clear()
    app.notes.extend([
        {"title": "Note A", "body": "Python is great"},
        {"title": "Note B", "body": "Unrelated content"},
    ])
    r = client.get("/?q=Python")
    assert b"Note A" in r.data
    assert b"Note B" not in r.data


def test_search_case_insensitive(client, app):
    app.notes.clear()
    app.notes.append({"title": "UPPERCASE Title", "body": "Some body text"})
    r = client.get("/?q=uppercase")
    assert b"UPPERCASE Title" in r.data


def test_empty_search_shows_all(client, app):
    app.notes.clear()
    app.notes.extend([
        {"title": "First note", "body": "Body one"},
        {"title": "Second note", "body": "Body two"},
    ])
    r = client.get("/?q=")
    assert b"First note" in r.data
    assert b"Second note" in r.data
