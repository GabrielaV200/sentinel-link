import requests
from requests import exceptions
import types
import pytest

from src.ingestion import api_ingester


class DummyResponse:
    def __init__(self, status_code=200, data=None):
        self.status_code = status_code
        self._data = data or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")

    def json(self):
        return self._data


def test_fetch_json_success(monkeypatch):
    calls = {"n": 0}

    def fake_get(url, timeout):
        calls["n"] += 1
        return DummyResponse(200, {"ok": True, "url": url})

    monkeypatch.setattr(requests, "get", fake_get)
    res = api_ingester.fetch_json("http://example.com")
    assert res["ok"] is True
    assert calls["n"] == 1


def test_fetch_json_retries_then_success(monkeypatch):
    sequence = [exceptions.RequestException("down"), exceptions.RequestException("down2"), DummyResponse(200, {"ok": True})]

    def fake_get(url, timeout):
        v = sequence.pop(0)
        if isinstance(v, Exception):
            raise v
        return v

    monkeypatch.setattr(requests, "get", fake_get)
    res = api_ingester.fetch_json("http://example.com")
    assert res["ok"] is True


def test_safe_fetch_default_on_failure(monkeypatch):
    def fake_get(url, timeout):
        raise exceptions.RequestException("nope")

    monkeypatch.setattr(requests, "get", fake_get)
    res = api_ingester.safe_fetch("http://bad.url", default={"ok": False})
    assert res == {"ok": False}
