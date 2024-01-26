from song import Song

class SerializerBase:
    def to_str(self, song: Song)-> str:
        pass