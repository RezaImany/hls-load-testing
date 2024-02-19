from locust import HttpUser, task, between
import requests
import random
session = requests.Session()
#Put your stream master file address here
master_url =  "https://example.com/TEST/STREAM/master.m3u8"
session_url = master_url.rsplit('/', 1)[0]
master_response = session.get(master_url)
master_content = master_response.text
quality_list = [x for x in master_content.split('\n') if 'index.m3u8' in x]

class HLSUser(HttpUser):
    wait_time = between(1, 2)
    session = requests.Session()
    @task
    def get_variant_playlist(self):
        try:
            rand_quality = random.choice(quality_list)
            playlist_url = session_url + '/' + rand_quality
            playlist_response = self.session.get(playlist_url)
            playlist = playlist_response.text
            ts = [x for x in playlist.split('\n') if x.endswith('.ts')]
            ts_url = session_url + '/' + rand_quality.rsplit('/', 1)[0] + '/' + ts[-1]
            self.client.get(ts_url)
        except Exception as e:
            print(f"Error occurred: {e}")
