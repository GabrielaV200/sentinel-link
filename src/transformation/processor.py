from typing import List, Dict, Any, Tuple
from pydantic import BaseModel, ValidationError


class RecordModel(BaseModel):
    id: int
    value: str


def process(records: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Validate and process a list of records.

    Returns a tuple: (processed_records, errors)
    Each processed record includes `id`, `value`, `value_upper`, and `length`.
    """
    processed = []
    errors = []
    for i, r in enumerate(records):
        try:
            rec = RecordModel(**r)
            out = {
                "id": rec.id,
                "value": rec.value,
                "value_upper": rec.value.upper(),
                "length": len(rec.value),
            }
            processed.append(out)
        except ValidationError as exc:
            errors.append(f"record_{i}: {exc}")
    return processed, errors
