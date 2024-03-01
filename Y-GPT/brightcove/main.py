import os
import requests
import json
import subprocess
from dotenv import load_dotenv

load_dotenv()

pub_id = os.environ.get("account_ID")
client_id = os.environ.get("client_ID")
client_secret = os.environ.get("client_secret")
access_token_url = "https://oauth.brightcove.com/v4/access_token"
profiles_base_url = "https://cms.api.brightcove.com/v1/accounts/{pub_id}"

def get_access_token():
    access_token = None
    r = requests.post(access_token_url, params="grant_type=client_credentials", auth=(client_id, client_secret), verify=False)
    if r.status_code == 200:
        access_token = r.json().get('access_token')
        print(access_token)
    return access_token

def get_videos():
    access_token = get_access_token()
    headers = { 'Authorization': 'Bearer ' + access_token, "Content-Type": "application/json" }

    url = ("https://cms.api.brightcove.com/v1/accounts/{pubid}/videos/").format(pubid=pub_id)

    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        video_data = r.json()
        with open('video_data.json', 'w') as file:  
            json.dump(video_data, file, indent=4)
    
    return video_data

# get_videos()

def download_video(video_id: str):
    access_token = get_access_token()
    headers = { 'Authorization': 'Bearer ' + access_token, "Content-Type": "application/json" }
    url = ("https://cms.api.brightcove.com/v1/accounts/{pubid}/videos/{videoid}/sources").format(pubid=pub_id,videoid=video_id)

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        video_sources = r.json()
        for source in video_sources:
            src_value = source.get('src')
            print(src_value)
            if src_value:
                subprocess.run(["ffmpeg", "-i", src_value, f"tmp/{video_id}.mp4"])
                print("Video downloaded")
            return src_value
    else:
        print("failed")

# download_video("6309247301112")
# download_video(6330655456112)

def sources_through_refid(ref_id: str):
    access_token = get_access_token()
    headers = { 'Authorization': 'Bearer ' + access_token, "Content-Type": "application/json" }
    url = ("https://cms.api.brightcove.com/v1/accounts/{pubid}/videos/ref:{ref_id}/sources").format(pubid=pub_id, ref_id=ref_id)

    r = requests.get(url, headers= headers)
    if r.status_code == 200:
        sources = r.json()
        with open('video_source.json','w') as file:
            json.dump(sources,file)
        print(sources)
    else:
        print("failed")

# sources_through_refid("MedePro_ETE_Test6")
