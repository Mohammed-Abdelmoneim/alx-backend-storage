#!/usr/bin/env python3
import redis
import uuid
"""exercise module"""


class Cache:
    """Cache class using redis"""

    def __init__(self):
        """init a new instance"""
        self._redis = redis.Redis()

    def store(self, data) -> str:
        id = uuid.uuid4()
        self._redis.set(str(id), data)
        return str(id)
