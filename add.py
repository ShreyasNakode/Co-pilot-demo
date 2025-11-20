def add(a, b):
    """Add two values. If native + fails, try numeric conversion to float.
    Raises TypeError with a clear message if values cannot be added."""
    try:
        return a + b
    except TypeError:
        try:
            return float(a) + float(b)
        except (TypeError, ValueError) as e:
            raise TypeError(f"Cannot add values {a!r} and {b!r}") from e
