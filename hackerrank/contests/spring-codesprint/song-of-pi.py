def celebrate(song):
    song_of_pi = True
    pi = "31415926535897932384626433833"
    for i in range(len(song)):
        if len(song[i]) != int(pi[i]):
            song_of_pi = False
    if song_of_pi:
        return "It's a pi song."
    else:
        return "It's not a pi song."

t = int(raw_input())

for case in range(t):
    song = [w for w in raw_input().split()]
    print celebrate(song)
