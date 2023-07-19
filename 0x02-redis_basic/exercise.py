#!/usr/bin/env python3
"""Create a Cache class."""
import redis
import uuid
from typing import Union


class Cache:
    """store an instance of the Redis client as
    a private variable named _redis
    (using redis.Redis()) and flush the instance using flushdb.
    """
    def __init__(self):
        """class definition."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, bytes, float, str]) -> str:
        """method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, int, bytes]:
        """Reading from Redis and recovering original type"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ automatically parametrize Cache.get to str """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get to int """
        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data
