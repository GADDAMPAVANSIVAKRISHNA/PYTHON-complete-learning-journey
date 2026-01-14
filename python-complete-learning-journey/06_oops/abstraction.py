"""Abstraction example: exposing a simple API"""

from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def store(self, key, value):
        pass

class MemoryStorage(Storage):
    def __init__(self):
        self._d = {}
    def store(self, key, value):
        self._d[key] = value


# Practice (5):
# 1) Create a `FileStorage` implementing `Storage` that writes JSON files.
# 2) Explain and demonstrate benefits of abstract base classes (interfaces).
# 3) Add a `retrieve(key)` method to the interface and implement it.
# 4) Show a case where composition is preferred over subclassing.
# 5) Write tests (simple assert) for `MemoryStorage` and `FileStorage`.
#
# Sample solutions (examples):
import json
class FileStorage(Storage):
    def __init__(self, path):
        self.path = path
        self._d = {}
    def store(self, key, value):
        self._d[key] = value
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self._d, f)
    def retrieve(self, key):
        return self._d.get(key)

if __name__ == "__main__":
    m = MemoryStorage()
    m.store('a', 1)
    f = FileStorage('store.json')
    f.store('a', 1)
    print('stored')
