from src.ingestion.loader import load_source
from src.transformation.transformer import transform


def test_loader_returns_list():
    data = load_source()
    assert isinstance(data, list)
    assert data and "id" in data[0]


def test_transformer_transforms():
    data = [{"id": 1, "value": "x"}, {"id": 2, "value": "y"}]
    out = transform(data)
    assert all(r.get("transformed") is True for r in out)
    assert out[0]["id"] == 1
