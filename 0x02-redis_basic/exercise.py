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
