# Concept: Class that stores a list and append
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        self.songs.append(title)
    def show(self):
        for song in self.songs:
            print(song)
    def length(self):
        song_list = len(self.songs)
        return song_list

my_playlist = Playlist("90's")
my_playlist.add_song("Yesterday")
my_playlist.add_song("She Bangs")
my_playlist.add_song("I pooped")
my_playlist.show()
print(my_playlist.length())