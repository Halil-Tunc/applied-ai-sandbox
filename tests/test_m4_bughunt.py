import pytest

from m4_bughunt import average_rating


def test_average_rating_rejects_empty_list():
    with pytest.raises(ValueError, match="ratings cannot be empty"):
        average_rating([])
