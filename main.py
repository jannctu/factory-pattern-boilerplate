from serializer_provider import SerializerProvider
from json_serializer import JsonSerializer
from xml_serializer import XmlSerializer
from serializer_enum import SerializerEnum

from song import Song



def main():
    song1 = Song('1', 'Water of Love', 'Dire Straits')
    
    serializer_factory = SerializerProvider()
    serializer_factory.register(SerializerEnum.JSON, JsonSerializer())
    serializer_factory.register(SerializerEnum.XML, XmlSerializer())


    serializer = serializer_factory.get(SerializerEnum.JSON)

    print(serializer.to_str(song1))

if __name__ == "__main__":
    main()