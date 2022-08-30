import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIPY_CLIENT_ID="add419895c1f4fd09ed9638c2858f10e"
# SPOTIPY_CLIENT_SECRET="271b39b9429d4a319858ef19db87289a"
# SPOTIPY_REDIRECT_URI="http://0.0.0.0:44444/callback/"

def loginProcess():
  scope = "user-top-read"

  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                                cache_handler=MemoryCacheHandler(
                                                  token_info=TOKEN_INFO
                                                )))

  userTopTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
  globalTopTracks = sp.playlist_items('37i9dQZEVXbMDoHDwVN2tF')

  userSet = set()
  for item in userTopTracks['items']:
      userSet.add(item['artists'][0]['name'] + " - " + item['name'])
  # print(userSet)

  # print("\n\n\n\n")

  globalSet = set()
  for item in globalTopTracks['items']:
    track = item['track']
    globalSet.add(track['artists'][0]['name'] + " - " + track['name'])
  # print(globalSet)

  basicSet = userSet.intersection(globalSet)

  # print("\n\n\n\n")
  # print(basicSet)
  # print("\n\n\n\n")
  # print(str(int((len(basicSet)/50 * 100))))# + "% basic")
  return int((len(basicSet)/50 * 100))

############################
# put global top 50 tracks into dictionary
# put user top 50 tracks into dictionary
# for track in enumerate(userTopTracks)
#   if track in globalTopTracks 
#       add 1 to mainstreamCount
# print(str(mainstream count / 50 * 100) + "% mainstream")