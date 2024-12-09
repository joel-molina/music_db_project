#Famous Favorite Songs App
#Created by: Joel Molina

#custom imports
import login
import music

class Session:
    def __init__(self):
        self.login = login.Login()
        self.music = music.Music()
        self.choice = None
        
    def display_title(self):
        print("Welcome to the Famous Favorite Songs App")


    def display_main_menu(self):
        print('''
                1. Add a favorite song
                2. Delete a favorite song
                3. View list of favorite songs
                4. View top charts information for favorite songs
                5. Get musical attributes of favorite songs
                6. Determine a song recommendation 
                0. Exit
                ''')


    def main_flow(self):
        while(self.choice != 0):
            self.display_main_menu()
            self.choice = int(input("Select an option: "))

            if(self.choice == 1):
                self.music.add_favorite_song(self.login.user.email)
            elif(self.choice == 2):
                self.music.delete_favorite_song(self.login.user.email)
            elif(self.choice == 3):
                self.music.display_favorite_songs(self.login.user.email)
            elif(self.choice == 4):
                self.music.display_charts_information(self.login.user.email)
            elif(self.choice == 5):
                self.music.display_favorite_song_attributes(self.login.user.email)
            elif(self.choice == 6):
                self.music.make_music_recommendation(self.login.user.email)
            elif(self.choice == 0):
                break
            else:
                print("Enter a valid option.")


def main():
    session = Session()
    session.login.login_flow()
    session.main_flow()

if __name__ == "__main__":
    main()