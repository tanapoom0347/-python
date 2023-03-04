# Python 3.6 - Fomatted string litterals

def demo():
    track = "Perfect"
    artist = "Ed Sheeran"
    album = "devide"
    download = 127
    print(f"track name = {track}, artist = {artist}, download = {download:,}") # string interpolation
    print("track name = {}, artist = {}".format(track, artist))

if __name__ == '__main__':
    demo()