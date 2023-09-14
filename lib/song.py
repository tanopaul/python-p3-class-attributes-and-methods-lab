class Song:

    count = 0
    all = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.increase_count()
        Song.add_songs(self)
        Song.add_genres(genre)
        Song.add_artist(artist)

    @classmethod
    def increase_count(cls, increment=1):
        cls.count+=increment
        
    @classmethod
    def add_songs(cls, song):
        cls.all.append(song)

    @classmethod
    def add_genres(cls, genre):
        cls.genres.append(genre)
        cls.genre_count[genre] = cls.genres.count(genre)

    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)
        cls.artist_count[artist] = len([song.artist for song in cls.all if song.artist == artist])


    
        

# song = Song('a', 'b', 'Rap')
# song1 = Song('d', 'e', 'Country')
# song2 = Song('g', 'h', 'Hip Hop')
# Song.genres
# Song.count

