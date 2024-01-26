import enum 

class SerializerEnum(str, enum.Enum):
    JSON = "JSON"
    XML = "XML"
    