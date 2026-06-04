"""Stub transformation module"""

def transform(records):
    """Apply a trivial transformation to records (stub)."""
    return [{**r, "transformed": True} for r in records]
