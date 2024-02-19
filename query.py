import pickle

with open("songs.pickle", "rb") as f:
    songs = pickle.load(f)

query = "poet"

filtered = [song for song in songs if query in song["text"]]
for song in filtered:
    print(song["name"])
    print(song["text"])
