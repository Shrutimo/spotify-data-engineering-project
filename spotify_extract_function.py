import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import os
import boto3

def lambda_handler(event, context):
    id = os.environ.get('client_id')
    secret = os.environ.get('client_key')
    
    client_credentials = SpotifyClientCredentials(client_id = id , client_secret = secret)
    spot_object = spotipy.Spotify(client_credentials_manager= client_credentials)
    
    playlist_url = 'https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg'
    playlist_id = playlist_url.split("/")[-1]
    data = spot_object.playlist_tracks(playlist_id)
    
    client = boto3.client('s3')
    file_name = "spotify_raw_data_" + str(datetime.now())+".json"
    
    client.put_object(
        Bucket = "spotify-data-pipeline-shruti",
        Key = "raw_data/to_process_files/" + file_name,
        Body = json.dumps(data)
        )
    # TODO implement
    
