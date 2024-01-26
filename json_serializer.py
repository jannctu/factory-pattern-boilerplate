import json
from song import Song
from serializer_base import SerializerBase

class JsonSerializer(SerializerBase):
    def to_str(self, song: Song):
        song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
        return json.dumps(song_info)
