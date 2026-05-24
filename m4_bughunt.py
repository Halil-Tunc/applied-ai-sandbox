def average_rating(ratings):
    """Return the average of a list of ratings."""
    if not ratings:
        raise ValueError("ratings cannot be empty")
    return sum(ratings) / len(ratings)
