def BottlesofBeer(count):
    lyrics = ""
    while (count > 0):
        lyrics+= "{} bottles of beer on the wall, {} bottles of beer\nTakeonedown, pass it around\n" .format (count,count)
        count-=1
    return lyrics

if __name__ == "__main__":
    songLyrics = BottlesofBeer(99)
    print (songLyrics)