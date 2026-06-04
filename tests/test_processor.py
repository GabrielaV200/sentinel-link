from src.transformation.processor import process


def test_process_valid_records():
    records = [{"id": 1, "value": "abc"}, {"id": 2, "value": ""}]
    processed, errors = process(records)
    assert len(processed) == 2
    assert errors == []
    assert processed[0]["value_upper"] == "ABC"
    assert processed[1]["length"] == 0


def test_process_invalid_records():
    records = [{"id": "x", "value": "abc"}, {"value": "no id"}]
    processed, errors = process(records)
    assert len(processed) == 0
    assert len(errors) == 2
    assert "record_0" in errors[0]
    assert "record_1" in errors[1]


def test_process_empty_list():
    processed, errors = process([])
    assert processed == []
    assert errors == []
