from random import randrange, seed
from datetime import datetime


class Playlist:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.length = 0
        self.videos = []

    def new_video(self, artist_name, song_name, song_length):
        if self.length == 0:
            self.length += song_length
        else:
            total = self.length + song_length
            seconds = (total - int(total))
            if seconds >= 0.60:
                total += 1
                total -= 0.60
                self.length = total
            else:
                self.length = total

        new_video = f"{artist_name}, {song_name}, {str(song_length)}"
        self.videos.append([f"Video No.{len(self.videos) + 1}: {new_video}"])

    def __str__(self):
        return f"Title: {str(self.title)}\n" \
               f"Description: {str(self.description)}\n" \
               f"Length: {str(round(self.length, 2))}"

    def recommendation(self):
        random_video = self.videos[randrange(len(self.videos)-1)]
        return random_video


class ClassicalPlaylist(Playlist):
    def __init__(self, title, description, playlist_era):
        super().__init__(title, description)
        self.era = playlist_era
        self.length = 0
        self.videos = []

    def recommendation(self):
        return self.videos[0]


playlist1 = Playlist("Playlist 1", "My Favorite Artists")

playlist1.new_video("Pitou", "His Song", 3.14)
playlist1.new_video("Daughter", "Love", 5.44)
playlist1.new_video("Luwten", "Element of Surprise", 3.21)
playlist1.new_video("Taylor Swift", "Style", 3.51)
print(playlist1)
print(playlist1.videos)

playlist2 = ClassicalPlaylist("Playlist 2", "Vibing", "Mostly Pop")

playlist2.new_video("Doja Cat", "Say So", 3.58)
playlist2.new_video("Maroon 5", "Closure", 11.29)
playlist2.new_video("Ayo & Teyo", "Fly N Ghetto", 2.29)
print(playlist2)
print(playlist2.videos)

print(playlist1.recommendation())
print(playlist2.recommendation())

