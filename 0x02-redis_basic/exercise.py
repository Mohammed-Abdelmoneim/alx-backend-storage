#!/usr/bin/env python3
import redis
from typing import Union
import uuid
"""exercise module"""


class Cache:
    """Cache class using redis"""

    def __init__(self):
        """init a new instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = uuid.uuid4()
        self._redis.set(str(id), data)
        return str(id)
