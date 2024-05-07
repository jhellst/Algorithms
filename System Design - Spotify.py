# Spotify: System Design
#   - Pseudocoded response, with data structures outlined in Python

# Spotify:

# Requirements:
#   - A user can choose any song in the song library (no need to upload songs)
#   - Users can save songs to playlists
#   - Each song should be attached to an album
#   - Albums include songs AND cover art.

# Methods:
#   - Create playlist
#   - Add song to playlist
#   - Play song -> Abstracted from some external API.

# Questions:
#   - Do you have to create a playlist before adding songs to it?
#   - Are we assuming that a user can only add to their own playlist? -> Yes.
#       - Can a playlist only be viewed or played by the creator? -> Maybe, consider later.
#   - Do we want to have a queue for playing songs? -> Maybe (Yes, if time).
#   - Are we assuming that the active user is already logged in? -> Yes, but we need to store all users within the


class Spotify:
    def __init__(self, songs_list: dict, users_list: dict, playlists: dict):
        self.songs = songs_list # dict that contains each song paired to a unique name/id.
        self.users = users_list
        self.playlists = playlists # Are these included on the spotify level, only? Are they connected to users?

    # Methods:

    def add_song_to_playlist(self, song, playlist_name):
        # Add song to self.songs. Error check to ensure the song isn't already in the playlist.
        song_name = song.name # Unique name/id for the song.
        self.songs[song_name] = song
        self.playlists[playlist_name].songs[song_name] = song

    def create_playlist(self, playlist_name):
        # Error check to ensure that we're creating a new playlist (and the same name/id hasn't been used).
        # Then, create the playlist and save it.
        newPlaylist = Playlist(playlist_name)
        self.playlists[playlist_name] = newPlaylist

    def play_song(song):
        # Plays the song via audio.

class Playlist:
    def __init__(self, playlist_name, songs={}):
        self.name = playlist_name
        self.songs = songs

class User:
    def __init__(self, username, playlists: dict):
        self.playlists = playlists # Dict that pairs every playlist for lookup via a unique key/id.
        self.username = username

