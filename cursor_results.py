#File containing classes to convert cursor results into complete objects

class Email:
    def __init__(self):
        self.email = None

    #used in user.py
    def convert_email_result(self, row):
        if row is None:
            self.email = None
        else:
            self.email = row[0]

class Track:
    def __init__(self):
        self.track_name = None
        self.artist = None
        self.released_year = None
        self.streams = None

        def convert_name_artist_results(self, rows):
            pass