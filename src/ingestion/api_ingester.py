from typing import Any, Dict, Optional
import requests
from requests import exceptions
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


@retry(stop=stop_after_attempt(3), wait=wait_fixed(0.1), retry=retry_if_exception_type(exceptions.RequestException))
def fetch_json(url: str, timeout: float = 5.0) -> Dict[str, Any]:
    """Fetch JSON from a URL, retrying on request exceptions.

    Raises the underlying exception if all retries fail.
    """
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def safe_fetch(url: str, default: Optional[Any] = None, timeout: float = 5.0) -> Any:
    """Fetch JSON but return `default` if fetching fails after retries."""
    try:
        return fetch_json(url, timeout=timeout)
    except Exception:
        return default
