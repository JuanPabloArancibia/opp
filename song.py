class Song:
    """
    Class to represent a song
        Attributes:
            title (str): The title of the song
            artist (str): An artist object representing the songs creator.
            duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method
        Args:
            str title:
            :param artist:
            :param duration:
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Albums:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album created.
        artist (str): The artist responsible for the album.
        If not specified,the artist will default to an artist with the name "Various Artist".
        tracks: (List[Song]): A list of the song on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the track list

        :param song: The title of the song to add.
        :param position: (Optional[int]): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        :return:
        """
        song_found = find_data(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list icludes only those albums in this collection, it is
            not an exhautive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list

    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list
        Args:
            album (Album): Album object to add to the list.
                If the album is ready present, it will not added again (although this is yet implemented)

        """

        self.albums.append(album)

    def add_song(self, name, year, title):
        """

        :param name: The name of the album
        :param year: Year of the album
        :param title: name of the song
        :return:
        """
        album_found = find_data(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Albums(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Album found " + name)

        album_found.add_song(title)


def find_data(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_data(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)
