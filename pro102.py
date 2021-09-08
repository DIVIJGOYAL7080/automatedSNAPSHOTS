import time
import snapshot

start_time = time.time()
access_token = input("Dropbox Access Token: ")

while True:
    if (time.time() - start_time) >= 5:
        name = snapshot.take_snapshot()
        snapshot.upload_snapshot(name, access_token)