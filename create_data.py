import pickle
import json

songs = []
with open("songs.jsonlines", "r") as f:
    line = f.readline()
    while line:
        song = json.loads(line)
        if song["name"] not in [s["name"] for s in songs]:
            song["text"] = song["text"].lower().replace("\n", " ")
            songs.append(song)
        line = f.readline()

with open("songs.pickle", "wb") as f:
    pickle.dump(songs, f)