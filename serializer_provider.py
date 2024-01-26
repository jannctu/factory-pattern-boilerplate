from serializer_base import SerializerBase

class SerializerProvider:
    def __init__(self):
        self._serializers = {}

    def register(self, key:str, serializer:SerializerBase):
        self._serializers[key] = serializer

    def get(self, key) -> type[SerializerBase]:
        serializer = self._serializers.get(key)
        if not serializer:
            raise ValueError(key)
        return serializer