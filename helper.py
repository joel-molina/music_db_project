#File containing classes to convert cursor results into complete objects, when applicable/practical.
#Also contains user attribute setters to support login capabilities for a user.

import db_connection

class User:
    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None


    def set_email(self, new_or_existing):
        #initialize connection
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        self.email = input("Enter your email: ")

        #check that email does not already exist.
        if(new_or_existing == 0): #0 meaning new
            cursor = self.connection.cursor()
            cursor.execute('''
                            SELECT "User".email
                            FROM "User"
                            WHERE "User".email = %s;
                            ''', (self.email,))
            result = cursor.fetchone()
            cursor.close()
            self.connection.close()

            if result is None:
                return 1 #valid email.
            else:
                return 0 #invalid email.
        
        #existing user, return the email.
        return self.email
        

    def set_first_name(self):
        self.first_name = input("Enter your first name: ")


    def set_last_name(self):
        self.last_name = input("Enter your last name: ")


    #convert user query result to object
    def convert_results(self, row):
        if row is None:
            self.email = None
            self.first_name = None
            self.last_name = None
        else:
            self.email = row[0]
            self.first_name = row[1]
            self.last_name = row[2]



class Track:
    def __init__(self):
        self.track_name = None
        self.artist = None
        self.released_year = None
        self.streams = None

    #convert track query result to object
    def convert_results(self, row):
        if row is None:
            #not necessary to set attributes to none since rows are checked for null.
            #helps prevent unintended side effects in any future expansions.
            self.track_name = None
            self.artist = None
            self.streams = None
            self.released_year = None
        else:
            self.track_name = row[0]
            self.artist = row[1]
            self.streams = row[2]
            self.released_year = row[3]
