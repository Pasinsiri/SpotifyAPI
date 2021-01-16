import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# * User-defined functions
from functions.load_keys import load_api_key

# client_id = '0fa683ab3a2c4ff6982f77b266d9e758'
# client_secret = 'ba1b9faa5b544d82bf283a65c7d85314'
client_id, client_secret = load_api_key()

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_track_id(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = get_track_id('pasinsiri', 'spotify:playlist:2AuI9hydgC3HeeX2HA0N30')

# print(len(ids))

def get_track_features(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    # ? Meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # ? Features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

# TODO: Loop Over Track IDs
tracks = []
for track_id in ids:
    time.sleep(.5)
    track = get_track_features(track_id)
    tracks.append(track)

# * Create dataset
df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv('data/spotify.csv', sep = ',', index = False)