import db_connection

class Music:
    def add_favorite_song(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        song_name = input("Enter the title of a favorite song: ")
        song_name = song_name.lower()
        artists = input("Enter song artist(s): ")
        artists = artists.lower()


        #find song based off of title AND artist(s)
        cursor = self.connection.cursor()
        cursor.execute('''
                        SELECT track_id
                        FROM "Track"
                        WHERE LOWER(track_name) = %s AND LOWER("artist(s)_name") = %s;
                        ''', (song_name, artists))
        track = cursor.fetchone()

        if track is None:
            print("Song is not in the top 1000 songs for 2024.")
        else: 
            track_id = track[0]
            #check track isn't already in favorites table
            cursor.execute('''
                            SELECT email, track_id
                            FROM "Favorite"
                            WHERE email = %s AND track_id = %s;
                            ''', (email, track_id))
            favorite = cursor.fetchone()

            if favorite is None:
                #add to favorites table
                cursor.execute('''
                                INSERT INTO "Favorite" (email, track_id)
                                VALUES (%s, %s);
                                ''', (email, track_id)) 
                print("Song added!")
            else: 
                print("Song is already in your favorites!")

        cursor.close()
        self.connection.commit()
        self.connection.close()

    
    def delete_favorite_song(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        song_name = input("Enter title of the song to be deleted from favorites list: ")
        song_name = song_name.lower()
        artists = input("Enter artist(s) of song to be deleted: ")
        artists = artists.lower()

        #check song is valid
        cursor = self.connection.cursor()
        cursor.execute('''
                        SELECT track_id 
                        FROM "Track"
                        WHERE LOWER(track_name) = %s AND LOWER("artist(s)_name") = %s;
                        ''', (song_name, artists))
        track = cursor.fetchone()

        if track is None:
            print("Song is not in the top 1000 songs for 2024.")
        else:
            track_id = track[0]
            #check that track is in favorites table
            cursor.execute('''
                            SELECT email, track_id
                            FROM "Favorite"
                            WHERE email = %s AND track_id = %s;
                            ''', (email, track_id))
            favorite = cursor.fetchone()

            if favorite is None:
                print("Song is not in your list of favorites!")
            else:
                #delete from Favorite table
                cursor.execute('''
                                DELETE FROM "Favorite"
                                WHERE email = %s AND track_id = %s;
                                ''', (email, track_id))
                print("Song deleted!")
        
        cursor.close()
        self.connection.commit()
        self.connection.close()


    def display_favorite_songs(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        cursor = self.connection.cursor()
        cursor.execute('''
                        SELECT track_name, "artist(s)_name", streams, released_year
                        FROM "Track"
                        JOIN "Favorite" ON "Track".track_id = "Favorite".track_id
                        WHERE "Favorite".email = %s;
                        ''', (email,))
        
        results = cursor.fetchall()
        cursor.close()
        self.connection.close()

        if results is None:
            print("You have no favorite songs yet!")
        else:
            print("Favorite songs: [Name, artist(s), # of streams, release year]")
            for i in range(len(results)):
                print(results[i])


    def display_charts_information(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        cursor = self.connection.cursor()
        cursor.execute('''
                        SELECT "Track".track_name, "Track"."artist(s)_name", 
                        "Charts".in_spotify_charts, "Charts".in_apple_charts, "Charts".in_shazam_charts
                        FROM "Track"
                        JOIN "Favorite" ON "Track".track_id = "Favorite".track_id 
                        JOIN "Charts" ON "Track".track_id = "Charts".track_id
                        WHERE "Favorite".email = %s;
                        ''', (email,))
        
        results = cursor.fetchall()
        cursor.close()
        self.connection.close()

        if results is None:
            print("You have no favorite songs yet!")
        else:
            print("Favorite songs AND their peak position on the spotify, apple, shazam charts:")
            for i in range(len(results)):
                print(results[i])


    def display_favorite_song_attributes(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        cursor = self.connection.cursor()
        cursor.execute('''
                        SELECT "Track".track_name, "Track"."artist(s)_name", 
                        "MusicalAttributes".bpm, "MusicalAttributes".key,
                        "MusicalAttributes".mode, "MusicalAttributes"."danceability_%%", 
                        "MusicalAttributes"."energy_%%"
                        FROM "Track"
                        JOIN "Favorite" ON "Track".track_id = "Favorite".track_id 
                        JOIN "MusicalAttributes" ON "Track".track_id = "MusicalAttributes".track_id
                        WHERE "Favorite".email = %s;
                        ''', (email,))
        
        results = cursor.fetchall()
        cursor.close()
        self.connection.close()

        if results is None:
            print("You have no favorite songs yet!")
        else:
            print("Favorite songs AND their bpm, key, mode, danceability%, and energy%:")
            for i in range(len(results)):
                print(results[i])


    def make_music_recommendation(self, email):
        db_c = db_connection.Connect()
        self.connection = db_c.get_connection()

        #select most similar score
        cursor = self.connection.cursor()
        #determine avg danceability and energy for favorite songs
        cursor.execute('''
                        SELECT AVG("danceability_%%") AS avg_f_danceability,
                               AVG("energy_%%") AS avg_f_energy
                        FROM "MusicalAttributes"
                        JOIN "Track" ON "MusicalAttributes".track_id = "Track".track_id 
                        JOIN "Favorite" ON "Track".track_id = "Favorite".track_id 
                        WHERE "Favorite".email = %s;
                        ''', (email,))
        favorites_result = cursor.fetchone()

        if favorites_result is None:
            print("You have no favorite songs yet!")
        else:
            f_score = favorites_result[0] + favorites_result[1]

            #determine danceability and energy for all songs, not including ones in favorite.
            cursor.execute('''
                            SELECT "MusicalAttributes"."danceability_%%", "MusicalAttributes"."energy_%%", 
                            "Track".track_name, "Track"."artist(s)_name"
                            FROM "MusicalAttributes"
                            JOIN "Track" ON "MusicalAttributes".track_id = "Track".track_id 
                            WHERE "Track".track_id NOT IN(
                            SELECT track_id
                            FROM "Favorite"
                            WHERE email = %s);
                            ''', (email,))
            track_results = cursor.fetchall()

            #get song with minimum score difference.
            minimum_difference = float("inf")
            best_track_name = None
            best_track_artist = None

            for i in range(len(track_results)):
                current_track_score = track_results[i][0] + track_results[i][1]
                
                difference = abs(f_score - current_track_score)
                if(difference < minimum_difference):
                    minimum_difference = difference
                    best_track_name = track_results[i][2]
                    best_track_artist = track_results[i][3]

            #display recommended song name and artist(s)
            print("Based on your favorite songs, a recommended song is: ", best_track_name, "by ", best_track_artist)

        cursor.close()
        self.connection.close()