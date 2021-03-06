from datetime import timedelta

from mtoolbox.cache import Cache, NoopCache


def test_get():
    cache = Cache("mtoolbox_test")
    cache.flush()

    assert cache.get("test", lambda: 1) == 1
    assert cache.get("test", lambda: 2) == 1
    assert cache.get("test", lambda: 2, invalidate=True) == 2
    assert cache.get("test", lambda: 1, maxage=timedelta(seconds=10)) == 2
    assert cache.get("test", lambda: 1, maxage=timedelta(seconds=0)) == 1

    cache.flush()
    assert cache.get("test", lambda: 3) == 3


def test_noop():
    cache = NoopCache("mtoolbox_test")

    assert cache.get("test", lambda: 1) == 1
    assert cache.get("test", lambda: 2) == 2
