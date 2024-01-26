import xml.etree.ElementTree as et
from song import Song
from serializer_base import SerializerBase

class XmlSerializer(SerializerBase):
    def to_str(sel, song: Song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')