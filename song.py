class Song:
    """ Class to represent a song

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
