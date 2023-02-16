import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def singleSearch(term:str):
    api_service_name = "youtube"
    api_version = "v3"
    KEY = 'AIzaSyAXZOBHx9YVGugbVTrSGemFxQ5S0nnSpp0'

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        order="relevance",
        q=term,
        type="video"
    )

    response = request.execute()
    videoId = response['items'][0]['id']['videoId']

    url = 'https://youtube.com/watch?v=' + videoId
    return url

    # print(type(test))
    # print('---------------------')
    # print('---------------------')
    # print(test)



