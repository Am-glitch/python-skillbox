class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}

    @property
    def cache(self):
        if not self.cache_dict:
            return None
        oldest_key = next(iter(self.cache_dict))
        return f"{oldest_key} : {self.cache_dict[oldest_key]}"

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            del self.cache_dict[key]
        elif len(self.cache_dict) >= self.capacity:
            del self.cache_dict[next(iter(self.cache_dict))]
        self.cache_dict[key] = value

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict.pop(key)
            self.cache_dict[key] = value
            return value
        else:
            return None


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
print(cache.cache)
