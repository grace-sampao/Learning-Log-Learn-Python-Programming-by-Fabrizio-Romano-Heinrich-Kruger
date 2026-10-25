class Client:
    def __init__(self):
        print("Setting up the client...")

    def query(self, **kwargs):
        print(f"Performing a query: {kwargs}")

class Manager:
    @property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

class ManualCacheManager:
    @property
    def client(self):
        if not hasattr(self, "_client"):
            self._client = Client()

        return self._client

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

from functools import cached_property

class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

print("--- Manager Class ---")
manager = Manager()
manager.perform_query()
manager.perform_query()

print("\n")

print("--- Manual Cache Manager Class ---")
manual_cache_manager = ManualCacheManager()
manual_cache_manager.perform_query()
manual_cache_manager.perform_query()

print("\n")

print("--- Cached Property Manager ---")
cached_property_manager = CachedPropertyManager()
cached_property_manager.perform_query(object_id=42)
cached_property_manager.perform_query(name_ilike="%Python%")

print("\n")

del cached_property_manager.client          # This causes a new client on next call
cached_property_manager.perform_query(age_gte=18)
