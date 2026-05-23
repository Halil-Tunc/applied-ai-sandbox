from app import parse_tags


def test_empty_string():
    assert parse_tags("") == []


def test_single_tag():
    assert parse_tags("work") == ["work"]


def test_two_tags():
    assert parse_tags("work, urgent") == ["work", "urgent"]


def test_whitespace_and_blanks():
    assert parse_tags(" work , , urgent , ") == ["work", "urgent"]
