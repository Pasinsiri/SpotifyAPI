from __future__ import print_function
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

# * User-defined functions
from functions.load_keys import load_api_key
client_id, client_secret = load_api_key()

client_creds_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_creds_manager)

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    tid = 'spotify:track:4TTV7EcfroSLWzXRY6gLv6'

start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start 
print(json.dumps(analysis, indent=4))
print('Analysis Retrieved in %.2f seconds' % (delta,))